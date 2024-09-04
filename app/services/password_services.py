from fastapi import status, HTTPException
from passlib.context import CryptContext


def hash_password(password):
    crypt_context = CryptContext(schemes=['sha256_crypt'])
    return crypt_context.hash(password)


def validation_password(password, password_registred):
    crypt_context = CryptContext(schemes=['sha256_crypt'])
    
    if crypt_context.verify(password, password_registred):
        return "token jwt"
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Email or password is incorrect")
