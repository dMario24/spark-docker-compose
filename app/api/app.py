from fastapi import FastAPI, WebSocket
import uvicorn
import asyncio
import random

app = FastAPI()

# 랜덤 문장을 생성하는 함수
def generate_random_sentence():
    sentences = [
        "Hello, welcome to the server!",
        "How's your day going?",
        "Here’s a random thought for you.",
        "FastAPI is fun and powerful!",
        "Did you know? Python is named after Monty Python."
    ]
    return random.choice(sentences)

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connection established.")
    try:
        while True:
            # 랜덤 문장을 생성하고 클라이언트로 전송
            random_sentence = generate_random_sentence()
            await websocket.send_text(random_sentence + "\n")
            print(f"Sent: {random_sentence}")
            # 2초 대기 후 다음 메시지 전송
            await asyncio.sleep(2)
    except Exception as e:
        print(f"Connection closed: {e}")
    finally:
        await websocket.close()
        print("WebSocket connection closed.")
