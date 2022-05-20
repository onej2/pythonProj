# DVD 재고관리
# 1. DVD 추가 2. DVD 수정 3. DVD 목록 4. DVD 구매 5. 프로그램 종료
# - DVD 추가 : DVD 이름과 가격을 입력받아서 저장
# - DVD 수정 : DVD 이름을 확인하고 있는 DVD에 가격을 입력받아 수정
# - DVD 목록 : 저장된 DVD명과 가격을 출력(천단위구분기호표기), DVD명 순서대로 출력
# - DVD 구매 : DVD 구매 시 거스름돈을 맞게 돌려주고 목록에서 삭제
# - 프로그램 종료 : 프로그램을 종료하는 메시지를 출력하고 종료
# - 메뉴1~5까지만 입력받고 다른 값이 들어오면 관련 에러 메시지를 출력한다.
# - 가격은 숫자로 입력해야됨

import json

f = open('DVD.json','r')
DVD = json.load(f)
f.close()

#DVD = {'핑구':50000, '짱구':70000, '패트와 매트':100000, '포켓몬스터':90000}
while True:
    choice = input('''
1. DVD추가  2. DVD수정  3. DVD목록  4. DVD구매  5. 프로그램종료
메뉴선택 >>> ''')
    if choice == '1':
        print('현재 DVD 목록 : ',list(DVD.keys()))
        name = input('추가할 DVD 제목을 입력하세요 >>>')
        price = 'a'
        while not price.isdecimal():
            price = input('추가할 DVD의 가격을 입력하세요 >>>')
        DVD[name] = int(price)
    elif choice == '2':
        print('현재 DVD 목록 : ',list(DVD.keys()))
        name = ''
        while not name in DVD.keys():
            name = input('수정할 DVD 제목을 입력하세요 >>>')
        price = 'a'
        while not price.isdecimal():
            price = input('수정할 DVD의 가격을 입력하세요 >>>')
        DVD[name] = int(price)
    elif choice == '3':
        print('------  DVD  ------')
        for item in sorted(DVD.items(), key=lambda data:data[1],reverse=True):
            print(f'{item[0]} : {item[1]:,}')
    elif choice == '4':
        print('현재 DVD 목록 : ',list(DVD.keys()))
        title=input('구매할 DVD 제목을 입력하세요 >>>')
        while not title in DVD:
                title = input('없는 DVD 입니다. 다시 입력하세요. >>>')
        price=DVD[title]
        print(f'DVD의 가격은 {price}원 입니다.')

        money=input('지불할 금액을 입력하세요 >>>')
        money=int(money)
        while money<price:
            money=int(input('금액이 부족합니다. 다시 입력하세요. >>>'))
        last=money-price
        print(f'잔돈은 {last}원 입니다.')
        name = ''
        print(f'{title}이(가) 목록에서 삭제됩니다.')
        del DVD[title]
    elif choice == '5':
        print('프로그램을 종료합니다.')
        f = open('DVD.json','w')
        json.dump(DVD,f)
        f.close()
        break
    else:
        print('메뉴를 잘못 선택 하셨습니다.')