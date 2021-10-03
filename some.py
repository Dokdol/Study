'''#랜덤값 사용한 리스트 출력 예제
import random

list = [ ]
for i in range(5):
    a = random.randint(0,10)
    list.append(a)
print(list)'''


#while문 반복 출력 예제
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")




