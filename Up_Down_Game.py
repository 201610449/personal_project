import random

def up_down_game(number_range):
    # 입력받은 number_range가 유효한지 검증
    if isinstance(number_range, int):
        if number_range <= 1:
            return print('잘못된 범위입니다.')
    else:
        return print('정수 범위를 지정해주세요.')
    
    highest_score = 0
    print(f'정답은 1 ~ {number_range}사이의 숫자입니다.')
    
    # 첫번째 while 루프: 게임의 재시작을 위한 반복문
    while True:
        if highest_score != 0:
            print(f'이전 게임의 최소 시도 횟수: {highest_score}')
        correct_number = random.randint(1, number_range)
        attempts = 0
        
        # 두번째 while 루프: 사용자가 정답을 맞출때까지 반복
        while True:
            # 세번째 while 루프: 사용자가 유효한 값을 입력할 때까지 반복
            while True:
                try:
                    input_number = int(input('숫자를 입력하세요.'))
                    if input_number > number_range or input_number < 1:
                        print(f'1 ~ {number_range}사이의 정수를 입력해주세요.')
                    else:
                        break # 세번째 while 루프 종료, 유효값 확인
                except ValueError:
                    print(f'1 ~ {number_range}사이의 정수를 입력해주세요.')
            attempts += 1 # 시도 횟수 증가
            
            if correct_number == input_number:
                print(f'정답입니다! 시도 횟수는 {attempts}번입니다.')
                break # 두번째 while 루프 종료, 이번 게임 종료
            else:
                if correct_number > input_number:
                    print('Up!')
                elif correct_number < input_number:
                    print('Down!')
                    
        # 하이스코어 업데이트
        if highest_score == 0: 
            highest_score = attempts
        else:
            highest_score = min([highest_score, attempts])
            
        # 네번째 while 루프: 재시작 여부 결정시, 입력값의 유효성을 검증
        while True:
            restart = input('다시 시작하시겠습니까? (Y/N)\n')
            restart = restart.upper()
            
            if restart == 'Y':
                break # 네번째 while 루프 종료, 첫번째 while 루프 반복으로 게임 재시작
            elif restart == 'N':
                return print(f'종료합니다. 최고기록은 {highest_score}입니다.') # return으로 함수 실행 종료, 모든 루프 종료
            else:
                print('잘못된 입력입니다.')

up_down_game(100) # 범위를 1 ~ 100으로 지정하고 게임을 시작