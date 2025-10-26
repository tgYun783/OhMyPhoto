import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. .env 파일에서 DB 접속 정보 읽어오기
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")

# 2. docker-compose 내부에서 접속할 DB 주소
#    localhost가 아니라 서비스 이름인 'db'를 사용합니다!
#    'postgresql://[유저이름]:[비밀번호]@[서비스이름]/[DB이름]'
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}"


# 3. SQLAlchemy 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 4. DB와 통신할 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. DB 모델(테이블)을 만들 때 사용할 기본 클래스
Base = declarative_base()