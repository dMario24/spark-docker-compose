FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 파일 복사 .dockerignore 파일 제외
COPY . ./

# Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너 실행 시 명령어
# uvicorn socket_fastapi:app --host 0.0.0.0 --port 8888
# fastapi dev socket_fastapi.py
# CMD ["uvicorn", "socket_fastapi:app", "--host", "0.0.0.0", "--port", "8888"]

CMD ["python", "socket_server.py"]
