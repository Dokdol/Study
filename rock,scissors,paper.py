import random


while True:
    player = input("가위,바위,보 중 하나를 입력하세요:")

    if player == '가위':
        break
    elif player == '바위':
        break
    elif player == '보':
        break
    else:
        print('잘못 입력했습니다. 다시 입력해주세요')
    

print('플레이어 : '+player) #빠져나온 player값을 출력
computer = random.choice(['가위', '바위', '보'])
print('컴퓨터 : '+computer) #이후 컴퓨터의 가위바위보 출력

if player == '가위': #if문을 통해 player와 computer 간 가위바위보에 따른 결과 출력
    if computer == '가위':
        print('결과 : 무승부')
    elif computer == '바위':
        print('결과 : 패배')
    else:
        print('결과 : 승리')

elif player == '바위':
    if computer == '가위':
        print('결과 : 승리')
    elif computer == '바위':
        print('결과 : 무승부')
    else:
        print('결과 : 패배')

else:
    if computer == '가위':
        print('결과 : 패배')
    elif computer == '바위':
        print('결과 : 승리')
    else:
        print('결과 : 무승부')