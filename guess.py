#시도회수를 최대 10변으로
#제한하려면 위의 프로그램을 어떻게 변경하여야 하는가?
import random
tries = 0
guess = 0
answer = random.randint(1, 100)
print("1부터 100사이의 숫자를 맞추시(기회는 10번) ")
while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries +1
    if guess < answer:
        print("정답보다 낮음 !더 올려!")
    if guess > answer:
        print("정답보다 높음 !더 내려!")
# while 문장을 벗어났을때 정답 맞았을때
#또는 10회 반봇하고 나서 (10회 제한)
if guess == answer:
    print("축하합니다. 시도 횟수=", tries)
else:#10회 제한으로 정답을 못맞추었을때
    print("10번 시도 끝!! 정답은 ", answer)