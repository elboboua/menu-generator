from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, constr
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os

router = APIRouter()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

# signup that takes email and password in json body and returns a token if the user is not already in the database
class SignupRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=100 )

@router.post("/signup")
async def signup(request: SignupRequest):
    email = request.email
    password = request.password

    jwt_claims = {
                    "sub": email, 
                    "exp": datetime.utcnow() + timedelta(days=365),
                    "id": 1
                }


    return {"jwt": generate_token(jwt_claims)}

    # check if user is already in the database





def generate_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

