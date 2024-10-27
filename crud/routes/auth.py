from fastapi import APIRouter

# from crud.models import User

# class User:
#     pass

router = APIRouter()


# @router.post("/login")
# def login(user_id: str):
#     # 로그인 로직 구현
#     return {"message": f"login id is {user_id}"}


# @router.post("/logout")
# def logout(user_id: str):
#     # 로그아웃 로직 구현
#     return {"message": f"logout id is {user_id}"}


# @router.post("/register")
# def register(user: User):
#     # 회원가입 로직 구현
#     return {"message": f"Registration successful: id: {user.id}"}


# @router.post("/withdraw")
# def withdraw(user_id: str, password: str):
#     def check_password(input_password: str):
#         # 비밀번호 체크 로직 구현
#         print(input_password)
#         return True
#     if not check_password(password):
#         # 회원 탈퇴 로직 구현
#         return {"message": f"Withdrawal successful: id: {user_id}"}
#     return {"message": "Incorrect password"}
