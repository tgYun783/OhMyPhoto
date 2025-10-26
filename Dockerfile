# 1. 기본이 될 파이썬 이미지를 가져옵니다.
FROM python:3.10-slim

# 2. 컨테이너 내부의 작업 폴더를 설정합니다.
WORKDIR /code

# 3. requirements.txt 파일을 먼저 복사하고 설치합니다.
# (파일이 변경되지 않으면 캐시를 사용해 빌드 속도가 빨라집니다)
COPY ./app/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 4. 나머지 앱 코드를 컨테이너에 복사합니다.
COPY ./app /code/app

# 5. 앱 실행 명령어 (개발 중에는 docker-compose에서 덮어쓸 예정)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]