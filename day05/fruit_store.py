# 과일가게 재고 프로그램
# 1. 과일 입력 2. 과일 판매 3. 과일 재고리스트 4. 과일 삭제 5. 프로그램 종료
# - 과일 입력 : 과일이름과 가격, 수량, 원가를 입력받아서 저장. 기존에 있는 과일이면 추가할 수량을 입력받아서 더해준다.
# - 과일 판매 : 과일을 팔았을 때의 이익을 계산하여 보여준다.
# - 과일 재고리스트 : 저장된 과일명과 가격을 출력하고 누적 수익을 보여준다.
# - 과일 삭제 : 목록에서 원하는 과일을 삭제한다.
# - 프로그램 종료 : 프로그램을 종료하는 메시지를 출력하고 종료한다.

import fruit_store_function as fsf

fruitlist=[]
fruitlist = [{'name' : '사과', 'price' : 1000, 'cost' : 500, 'count' : 2},
             {'name' : '바나나', 'price' : 2000, 'cost' : 800, 'count' : 3},
             {'name' : '오렌지', 'price' : 1400, 'cost' : 650, 'count' : 4}]

profit=0
pan=0

while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
1. 입력   2. 판매   3. 재고리스트   4. 삭제   5. 종료
>>> ''').upper()  

    if choice=="1":  
        cnt=fsf.fruit_input(fruitlist)
        
    elif choice=="2": 
        profit,pan=fsf.fruit_sale(fruitlist,profit,pan)

    elif choice == '3':
        fsf.fruit_list(fruitlist,profit)
        
    elif choice == '4':
        fsf.fruit_del(fruitlist)

    elif choice=="5":
        print('프로그램을 종료합니다.')
        break