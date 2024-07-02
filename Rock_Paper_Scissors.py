import random

def rock_paper_scissors():
    ROCK_PAPER_SCISSORS = ['가위', '바위', '보']
    win = 0
    draw = 0
    lose = 0
    
    while True:
        cpu_choice = random.choice(ROCK_PAPER_SCISSORS)
        
        while True:
            user_choice = input('가위, 바위, 보!\n')
            if user_choice in ROCK_PAPER_SCISSORS:
                break
            else:
                print('잘못된 입력입니다.')
        print(f'사용자:{user_choice}, 컴퓨터:{cpu_choice}')
        
        if user_choice == cpu_choice:
            print('무승부입니다.')
            draw += 1
        elif user_choice == '가위':
            if cpu_choice == '바위':
                print('컴퓨터 승리!')
                lose += 1
            elif cpu_choice == '보':
                print('사용자 승리!')
                win += 1
        elif user_choice == '바위':
            if cpu_choice == '보':
                print('컴퓨터 승리!')
                lose += 1
            elif cpu_choice == '가위':
                print('사용자 승리!')
                win += 1
        elif user_choice == '보':
            if cpu_choice == '가위':
                print('컴퓨터 승리!')
                lose += 1
            elif cpu_choice == '바위':
                print('사용자 승리!')
                win += 1
        print(f'현재 전적은 승리: {win} 패배: {lose} 무승부: {draw} 입니다.')
        
        while True:
            restart = input('계속하시겠습니까? (네/아니오)\n')
            
            if restart == '네':
                break
            elif restart == '아니오':
                print('종료합니다.')
                winning_rate= round((win + draw/2)/(win + lose + draw), 2)*100
                print(f'총 전적은 승리: {win} 패배: {lose} 무승부: {draw} 로 승률은 {winning_rate}% 입니다.')
                
                if winning_rate > 50:
                    result = '사용자의 승리입니다!'
                elif winning_rate < 50:
                    result = '사용자의 패배입니다..'
                else:
                    result = '무승부입니다.'
                return print(result)
            else:
                print('잘못된 입력입니다.')

rock_paper_scissors()