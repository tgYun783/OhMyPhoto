# Oh My Photo - 사진 클라우드 시스템 백엔드

## 개요

**Oh My Photo**는 사용자가 사진을 업로드, 저장, 관리할 수 있는 클라우드 기반 사진 관리 시스템의 백엔드 서버입니다.  
이 프로젝트는 FastAPI, SQLAlchemy, PostgreSQL, Docker를 활용하여 확장성과 유지보수성이 뛰어난 백엔드/데이터베이스 서버의 기초를 제공합니다.

---

## 주요 기술 스택

- **FastAPI**: 현대적이고 빠른 Python 웹 프레임워크 (RESTful API)
- **SQLAlchemy**: 파이썬 ORM(Object Relational Mapper)으로 데이터베이스 모델링 및 쿼리
- **PostgreSQL**: 신뢰성 높은 오픈소스 관계형 데이터베이스
- **Docker & Docker Compose**: 개발/운영 환경의 일관성 및 서비스 분리
- **Uvicorn**: ASGI 서버로 FastAPI 실행

---

## 시스템 아키텍처

```
[Client] <--REST API--> [FastAPI Backend] <--SQLAlchemy--> [PostgreSQL DB]
```

- 모든 서비스는 Docker 컨테이너로 분리되어 관리됩니다.
- 환경변수(.env)로 민감 정보 및 환경별 설정을 관리합니다.

---

## 주요 기능 (예정)

- 사진 업로드 및 다운로드 API
- 사진 메타데이터(파일명, 업로드 시각, 사용자 등) 관리
- 사용자 인증 및 권한 관리
- 사진 목록/검색/필터링 API
- API 문서 자동화 (Swagger/OpenAPI)
- 운영 환경 배포 및 데이터 영속화

---

## 폴더 구조

```
oh_my_photo/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI 진입점
│   ├── database.py        # DB 연결 및 ORM 설정
│   └── requirements.txt   # 파이썬 의존성 목록
├── Dockerfile             # 백엔드 컨테이너 빌드 설정
├── docker-compose.yml     # 전체 서비스 오케스트레이션
├── .gitignore             # Git 제외 파일 목록
└── .env                   # 환경변수 파일 (Git에 포함 X)
```

---

## 빠른 시작

1. `.env` 파일 생성  
   (예시)
   ```
   POSTGRES_USER=yourusername
   POSTGRES_PASSWORD=yourpassword
   POSTGRES_DB=yourdbname
   ```

2. Docker Compose로 서비스 실행
   ```bash
   docker-compose up --build
   ```

3. API 서버 접속  
   - 기본 주소: [http://localhost:8000](http://localhost:8000)
   - 자동 문서: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 향후 개발 계획

- 사진 업로드/다운로드 및 메타데이터 관리 API 구현
- 사용자 인증/인가 시스템 도입
- 테스트 코드 및 문서화 강화
- 클라우드 스토리지 연동(AWS S3 등) 지원

---

## 라이선스

MIT License
