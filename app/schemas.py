from pydantic import BaseModel, EmailStr

# --- User ---

# 회원가입 시 받을 데이터 (Request)
class UserCreate(BaseModel):
    email: EmailStr  # 이메일 형식인지 자동으로 검사해 줌
    password: str

# 사용자 정보 응답 시 사용할 데이터 (Response)
# hashed_password 처럼 민감한 정보는 빼고 보냄
class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True  # SQLAlchemy 모델을 Pydantic 모델로 변환 허용