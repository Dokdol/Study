import random


computer_num = []

strike_count = 0
ball_count = 0
out_count = 0



while len(computer_num) < 3:
    computer = random.randint(1,3)

    if (computer in computer_num) == False:
            computer_num.append(computer)
    else:
        pass

while strike_count < 3:
    while True:
        player_num = []
        player = input('0~9까지의 숫자 중 중복되지 않은 세 자리를 입력해주세요:')
        strike_count = 0
        ball_count = 0
        out_count = 0
        try_count = 0

        for i in range(0,3):
            player_num.append(player[i])
            
        if player_num[0] == player_num[1]:
            print('중복된 숫자가 입력되었습니다. 중복되지 않은 세 자리를 입력해주세요.')
        elif player_num[0] == player_num[2]:
            print('중복된 숫자가 입력되었습니다. 중복되지 않은 세 자리를 입력해주세요.')
        elif player_num[1] == player_num[2]:
            print('중복된 숫자가 입력되었습니다. 중복되지 않은 세 자리를 입력해주세요.')
        elif player_num[0] != player_num[1] != player_num[2]:
            pass

    for x in range(0,3):
        for y in range(0,3):
            if str(player_num[x]) == str(computer_num[y]) and x==y:
                strike_count+=1
                break
            elif str(player_num[x]) == str(computer_num[y]) and x!=y:
                ball_count+=1
                break
        else:
            out_count +=1

        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        print('스트라이크:', strike_count, '볼:', ball_count, '아웃:', out_count)
        print('시도 :', try_count)
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        
