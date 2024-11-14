import socket
import time
import random
from faker import Faker
fake = Faker()

def generate_random_message(word_count=50):
    """랜덤 메시지 생성: 중복 단어를 포함한 긴 문장"""
    words = [fake.word() for _ in range(word_count // 2)]  # 랜덤한 단어 목록 생성
    repeated_words = random.choices(words, k=word_count // 2)  # 일부 단어를 중복
    all_words = words + repeated_words
    random.shuffle(all_words)  # 단어 순서 섞기
    return ' '.join(all_words)


r = generate_random_message(100)
print(r)