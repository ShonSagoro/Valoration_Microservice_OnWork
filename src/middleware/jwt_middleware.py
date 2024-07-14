from fastapi import FastAPI, HTTPException, Header, Depends, Request
from fastapi.responses import JSONResponse
import jwt
import os

app = FastAPI()

SECRET_KEY = os.getenv('JWT_SECRET', 'your_default_secret_key')
ALGORITHM = "HS256"
blacklist = []

async def verify_token(request: Request):
    auth_header = request.headers.get('authorization')

    if not auth_header:
        raise HTTPException(status_code=401, detail="Token not provided")

    token = auth_header.split(' ')[1] if ' ' in auth_header else auth_header

    if not SECRET_KEY:
        raise HTTPException(status_code=500, detail="JWT secret not configured")

    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")