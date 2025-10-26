from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from . import database, models, schemas, security # database.py 임포트

# 애플리케이션 시작 시 DB 테이블 생성 (개발용)
# 나중에 Alembic 같은 도구로 대체하는 것이 좋습니다.
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# DB 세션을 가져오는 함수 (의존성 주입용)
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root(db: Session = Depends(get_db)):
    # .get_db()를 통해 DB 세션을 받아옵니다.
    # DB에 간단한 쿼리를 날려 연결을 테스트합니다.
    try:
        db.execute(text("SELECT 1"))
        return {"message": "사진 클라우드 백엔드 서버", "db_status": "connected_successfully!"}
    except Exception as e:
        # DB 연결 실패 시 에러 반환
        raise HTTPException(status_code=500, detail=f"DB 연결 실패: {e}")

@app.post("/users/signup", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """새로운 사용자 생성 (회원가입)"""
    
    # 1. 이메일 중복 확인
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이미 등록된 이메일입니다."
        )
    
    # 2. 비밀번호 해싱
    hashed_password = security.get_password_hash(user.password)
    
    # 3. 새 사용자 객체 생성 및 DB에 저장
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # DB에 저장된 ID 등 최신 정보로 객체 갱신
    
    return new_user