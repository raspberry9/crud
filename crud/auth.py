from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# a
# pp = FastAPI()
router = APIRouter()


class User(BaseModel):
    user_id: int
    username: str
    password: str
    email: str
    created_at: datetime
    updated_at: datetime
    is_active: bool


# http://127.0.0.1:8000/api/v1/auth/test
@router.get(f"/test")
def test():
    return {"hello": "world"}

@router.post("/login")
def login(user: User):
    # 로그인 로직 구현
    return {"message": "Login successful"}

@router.post("/logout")
def logout(user: User):
    # 로그아웃 로직 구현
    return {"message": "Logout successful"}

@router.post("/register")
def register(user: User):
    # 회원가입 로직 구현
    return {"message": "Registration successful"}

@router.post("/change-password")
def change_password(user: User, new_password: str):
    # 비밀번호 변경 로직 구현
    return {"message": "Password changed successfully"}

@router.post("/verify-email")
def verify_email(user: User):
    # 이메일 인증 로직 구현
    return {"message": "Email verified successfully"}

@router.post("/resend-email-verification")
def resend_email_verification(user: User):
    # 이메일 인증 재전송 로직 구현
    return {"message": "Verification email resent successfully"}

@router.post("/withdraw")
def withdraw(user: User):
    # 회원 탈퇴 로직 구현
    return {"message": "Withdrawal successful"}
