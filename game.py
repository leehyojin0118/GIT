import random
import time

print("======= 🤖 로봇 엔지니어의 숫자 맞추기 게임 =======")
print("1부터 30 사이의 컴퓨터의 숫자를 5번 안에 맞춰보세요!")
print("==================================================")

secret_number = random.randint(1, 30)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    # 사용자 입력 받기
    try:
        guess = int(input(f"[{attempts + 1}/{max_attempts}] 숫자를 입력하세요: "))
    except ValueError:
        print("❌ 숫자만 입력할 수 있습니다!")
        continue
    
    attempts += 1
    
    # 숫자 비교 (Up & Down)
    if guess < secret_number:
        print("▲ UP! 더 큰 숫자입니다.")
    elif guess > secret_number:
        print("▼ DOWN! 더 작은 숫자입니다.")
    else:
        print(f"🎉 축하합니다! {attempts}번 만에 맞추셨습니다!")
        break
else:
    print(f"💀 게임 오버! 정답은 {secret_number}였습니다.")

time.sleep(1)
print("==================================================")