from fastapi import FastAPI
import os

app = FastAPI()

# .env 파일에서 읽어온 DB 정보를 확인 (테스트용)
db_user = os.getenv("POSTGRES_USER", "없음")
db_name = os.getenv("POSTGRES_DB", "없음")

@app.get("/")
async def root():
    return {
        "message": "사진 클라우드 백엔드 서버",
        "db_user_check": db_user,  # docker-compose.yml을 통해 주입됨
        "db_name_check": db_name    # docker-compose.yml을 통해 주입됨
    }