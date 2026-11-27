"""R2.3: synthetic, in-memory cryptographic mechanisms, not an SSH implementation.
Requires an existing cryptography installation; no product dependency or real keys.
Only public-safe results are emitted; no files, network or configuration changes.
"""
import base64
import hashlib
import json
import os

from cryptography.exceptions import InvalidSignature, InvalidTag
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, padding, rsa, x25519
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


def rejected(operation, exception):
    try:
        operation()
    except exception:
        return True
    return False


def public_bytes(key):
    return key.public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)


def derive(shared):
    # Fixed public context label for this isolated exercise only.
    return HKDF(algorithm=hashes.SHA256(), length=32, salt=None,
                info=b"aegislab-r2.3-demo").derive(shared)


def main():
    message = b"hello"
    changed = b"Hello"
    digest = hashlib.sha256(message).hexdigest()
    altered_digest = hashlib.sha256(changed).hexdigest()
    encoded = base64.b64encode(message)
    result = {"encoding": {"base64": encoded.decode(), "roundtrip": base64.b64decode(encoded) == message},
              "hash": {"original": digest, "changed": altered_digest,
                       "same_input_same_digest": digest == hashlib.sha256(message).hexdigest(),
                       "changed_input_different_digest": digest != altered_digest}}

    # Symmetric authenticated encryption: a fresh nonce for this key.
    key = AESGCM.generate_key(bit_length=256)
    aes = AESGCM(key)
    nonce = os.urandom(12)
    encrypted = aes.encrypt(nonce, message, None)
    altered = bytes([encrypted[0] ^ 1]) + encrypted[1:]
    result["symmetric"] = {
        "roundtrip": aes.decrypt(nonce, encrypted, None) == message,
        "tamper_rejected": rejected(lambda: aes.decrypt(nonce, altered, None), InvalidTag),
        "wrong_key_rejected": rejected(lambda: AESGCM(AESGCM.generate_key(bit_length=256)).decrypt(nonce, encrypted, None), InvalidTag)}

    # Asymmetric encryption, distinct from signing and SSH session establishment.
    receiver = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    oaep = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    protected = receiver.public_key().encrypt(message, oaep)
    result["asymmetric_encryption"] = {"roundtrip": receiver.decrypt(protected, oaep) == message}

    # Signature checks bind bytes to possession of the signing private key,
    # not a person's identity absent an independently trusted public key.
    signer = ed25519.Ed25519PrivateKey.generate()
    other = ed25519.Ed25519PrivateKey.generate()
    verifier = signer.public_key()
    signature = signer.sign(message)
    verifier.verify(signature, message)
    result["signature"] = {
        "original_verified": True,
        "changed_message_rejected": rejected(lambda: verifier.verify(signature, changed), InvalidSignature),
        "other_public_key_rejected": rejected(lambda: other.public_key().verify(signature, message), InvalidSignature),
        "fingerprints_differ": hashlib.sha256(public_bytes(verifier)).digest() != hashlib.sha256(public_bytes(other.public_key())).digest()}

    # Unauthenticated ephemeral key agreement; no network and no SSH negotiation.
    alice, bob, unrelated = (x25519.X25519PrivateKey.generate() for _ in range(3))
    a = derive(alice.exchange(bob.public_key()))
    b = derive(bob.exchange(alice.public_key()))
    c = derive(alice.exchange(unrelated.public_key()))
    result["key_agreement"] = {"derived_keys_match": a == b, "different_peer_key_differs": a != c,
                               "derived_key_bytes": len(a), "peer_identity_authenticated": False}
    checks = [result["encoding"]["roundtrip"], result["hash"]["same_input_same_digest"],
              result["hash"]["changed_input_different_digest"], *result["symmetric"].values(),
              result["asymmetric_encryption"]["roundtrip"], *result["signature"].values(),
              result["key_agreement"]["derived_keys_match"], result["key_agreement"]["different_peer_key_differs"]]
    if not all(checks):
        raise RuntimeError("Unexpected cryptography exercise result")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
