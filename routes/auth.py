from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, constr
from bcrypt import hashpw, gensalt, checkpw
from jose import JWTError, jwt
from datetime import datetime, timedelta
from models import create_session, User
import os

router = APIRouter()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

# signup that takes email and password in json body and returns a token if the user is not already in the database
class SignupLoginRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=100 )

@router.post("/signup")
async def signup(request: SignupLoginRequest):
    email = request.email
    password = request.password

    db_session = create_session()
    user = db_session.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    hashed_password = hash_password(password)
    
    new_user = User(email=email, password=hashed_password)
    db_session.add(new_user)
    db_session.flush()
    user_id = new_user.id
    db_session.commit()



    jwt_claims = {
                    "sub": email, 
                    "exp": datetime.utcnow() + timedelta(days=365),
                    "id": user_id
                }

    token = generate_token(jwt_claims)

    # set the token as a cookie
    response = JSONResponse(content={"token": token})
    response.set_cookie(key="token", value=token, httponly=True)
    return response

@router.post("/login")
async def login(request: SignupLoginRequest):
    email = request.email
    password = request.password

    db_session = create_session()
    user = db_session.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to authenticate user")
    
    if not checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to authenticate user")
    
    jwt_claims = {
                    "sub": email, 
                    "exp": datetime.utcnow() + timedelta(days=365),
                    "id": user.id
                }
    
    # set the token as a cookie
    token = generate_token(jwt_claims)
    response = JSONResponse(content={"token": token})
    response.set_cookie(key="token", value=token, httponly=True)
    return response






def generate_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

def hash_password(password: str):
    return hashpw(password.encode('utf-8'), gensalt())