import random

def up_down_game(number_range):
    if isinstance(number_range, int):
        if number_range <= 1:
            return print('잘못된 범위입니다.')
    else:
        return print('정수 범위를 지정해주세요.')
    
    highest_score = 0
    print(f'정답은 1 ~ {number_range}사이의 숫자입니다.')
    
    while True:
        if highest_score != 0:
            print(f'이전 게임의 최소 시도 횟수: {highest_score}')
        correct_number = random.randint(1, number_range)
        attempts = 0
        
        while True:
            while True:
                try:
                    input_number = int(input('숫자를 입력하세요.'))
                    if input_number > number_range or input_number < 1:
                        print(f'1 ~ {number_range}사이의 정수를 입력해주세요.')
                    else:
                        break
                except ValueError:
                    print(f'1 ~ {number_range}사이의 정수를 입력해주세요.')
            attempts += 1
            
            if correct_number == input_number:
                print(f'정답입니다! 시도 횟수는 {attempts}번입니다.')
                break
            else:
                if correct_number > input_number:
                    print('Up!')
                elif correct_number < input_number:
                    print('Down!')
        
        if highest_score == 0:
            highest_score = attempts
        else:
            highest_score = min([highest_score, attempts])
        
        while True:
            restart = input('다시 시작하시겠습니까? (Y/N)\n')
            restart = restart.upper()
            
            if restart == 'Y':
                break
            elif restart == 'N':
                return print(f'종료합니다. 최고기록은 {highest_score}입니다.')
            else:
                print('잘못된 입력입니다.')

up_down_game(100)