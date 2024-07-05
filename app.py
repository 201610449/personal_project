import random
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.artist} {self.title} 추천 by {self.username}'

with app.app_context():
    db.create_all()

def rock_paper_scissors():
    ROCK_PAPER_SCISSORS = ['가위', '바위', '보']
    win = 0
    draw = 0
    lose = 0
    
    # 첫번째 while 루프: 게임의 재시작을 위한 반복문
    while True:
        cpu_choice = random.choice(ROCK_PAPER_SCISSORS)
        # 두번째 while 루프: 입력값의 유효성 검사
        while True:
            user_choice = input('가위, 바위, 보!\n')
            if user_choice in ROCK_PAPER_SCISSORS:
                break # 두번쨰 while 루프 종료, 유효값 확인
            else:
                print('잘못된 입력입니다.')
        print(f'사용자:{user_choice}, 컴퓨터:{cpu_choice}')
        
        # 가위바위보 결과 판정
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
        
        # 세번째 while 루프: 재시작 여부 결정시 유효성 검사
        while True:
            restart = input('계속하시겠습니까? (네/아니오)\n')
            
            if restart == '네':
                break # 세번째 while 루프 종료, 첫번째 while 루프 반복으로 게임 재시작
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