from sqlalchemy import Column, Integer, String
from .database import Base  # database.py 에서 정의한 Base 클래스 임포트

class User(Base):
    __tablename__ = "users"  # DB에 생성될 테이블 이름

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)