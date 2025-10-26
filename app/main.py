from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from . import database # database.py 임포트

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