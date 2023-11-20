# Unused at the moment, but used this to generate the jwks.json file
from jwcrypto import jwk

def build_jwks_from_public_pem():
    public_key = get_public_key()
    jwkey = jwk.JWK()
    jwkey.import_from_pem(public_key)
    jwks = {
        "keys": [jwkey.export(private_key=False)]
    }
    return jwks

def get_public_key():
    with open('../certs/publicKey.pem', 'rb') as pem_file:
        public_key = pem_file.read()
    return public_key

print(build_jwks_from_public_pem())