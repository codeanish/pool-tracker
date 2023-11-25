import jwt
from db.config import Config

def validate_token(token: str):
    jwks_client = jwt.PyJWKClient(Config.PUBLIC_KEYS_URL, cache_jwk_set=True, lifespan=360)
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    try:
        data = jwt.decode(
            token, 
            signing_key.key, 
            algorithms=['RS256'],
            options={
                    "verify_signature": True,
                    "verify_exp": True,
                    "verify_nbf": True,
                    "verify_iat": True,
                    "verify_aud": True,
                    "verify_iss": True,
                }
            )
        return data
    except jwt.exceptions.PyJWTError as err:
        print(err)
        return False

def get_user_from_token(token:str):
    payload = validate_token(token)
    if payload:
        return payload['sub']
    else:
        return None


if __name__ == "__main__":
    print(validate_token("eyJhbGciOiJSUzI1NiIsImtpZCI6IjIxME01WGMxclBEVWZKLS0zVi1zWnIxMlhmZ0FDN0xONjdzcGMxNF9zMEEiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJ0ZXN0MSIsImV4cCI6MTcwMDc0NTQxOH0.gWsFQ9lLgoH-sJGdOkNih6TBOIoF0Dw6OE8mHrcljdjRVlSdJ0FrWoxjOm3Sm6YWLg5lPtTxweo5Ti_K26w_Hqsxb0H3jk2wFVNN9y2u8Q_VQWGjKKXoaEcvJ9GPgowfZHzMmRDMInhSem2JqSj9PCaCTgI7LWnj13t-2dMkN_lPvdhWq3QH7IpPdUDKYBBGRaP8L6mc7JEoToQr5bLxY2sBcJhFt0NcyOxxj7ev4gL0whEAbxfLiY-IN3suzTPF7FUOSMlkCZDHPHLR-itx0Ze48nz_jEEPbJr4-s28hM65EcPrYBx5LgtxBmNGlqy75zJ2PmuhpQzVIAuJ5nmMvw"))