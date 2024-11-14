import socket
import time
import random
from faker import Faker
from faker import Faker
fake = Faker()

def generate_random_message(word_count=10):
    """랜덤 메시지 생성: 중복 단어를 포함한 긴 문장"""
    text = fake.text(max_nb_chars=word_count)
    return text.replace("\n", " ") + "\n"

def start_server(host='0.0.0.0', port=9999):
    # 소켓 객체 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버 주소와 포트 바인딩
    server_socket.bind((host, port))

    # 서버 소켓을 연결 대기 상태로 설정
    server_socket.listen(1)
    print(f"Listening on {host}:{port}...", flush=True)

    while True:
        # 클라이언트 연결 수락
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}", flush=True)

        with client_socket:
            while True:
                # 임의의 데이터를 클라이언트에게 주기적으로 전송
                word_count = random.randint(10, 10000000)
                message = f"{generate_random_message(word_count)}\n"
                client_socket.sendall(message.encode())
                print(f"Sent: {message}", flush=True)

                # n초마다 데이터를 전송
                time.sleep(random.randint(1, 60))

if __name__ == "__main__":
    start_server()