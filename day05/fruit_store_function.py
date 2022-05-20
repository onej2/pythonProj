def fruit_input(fruitlist):
    fruit={'name' : '', 'price' : '', 'cost' : '','count' : ''}
    while True:
        fruit['name'] = input('과일이름 입력 >>> ')
        for i in range(len(fruitlist)):
            if fruit['name'] in fruitlist[i]['name']:
                k = int(input('추가할 수량 입력 >>> '))
                nam = int(fruitlist[i]['count'])
                nam = nam + k
                fruitlist[i]['count'] = nam
                print('--------------------------  재고리스트  ----------------------------')
                print(*fruitlist,sep='\n')
                print('--------------------------------------------------------------------')
                break
            else:
                price = 'a'
                while not price.isdecimal():
                    fruit['price']=input('가격을 입력하세요.>>>')
                    break

                cost = 'b'
                while not cost.isdecimal():
                    fruit['cost']=input('원가를 입력하세요.>>>')
                    break

                count = 'c'
                while not count.isdecimal():
                    fruit['count']=input('수량을 입력하세요.>>>')
                    break
        
                
                fruitlist.append(fruit)
                print('--------------------------  재고리스트  ----------------------------')
                print(*fruitlist,sep='\n')
                print('--------------------------------------------------------------------')
                break
        break
    cnt=fruitlist[i]['count']
    return cnt

def fruit_sale(fruitlist,profit,pan):
    fruit={'name' : '', 'price' : '', 'cost' : '','count' : ''}
    while True:
        print('--------------------------  재고리스트  ----------------------------')
        print(*fruitlist,sep='\n')
        print('--------------------------------------------------------------------')
        fruit['name'] = input('과일이름 입력 >>> ')
        for i in range(len(fruitlist)):
            if fruit['name'] in fruitlist[i]['name']:
                k = int(input('판매한 과일 수 입력 >>> '))
                nam = int(fruitlist[i]['count'])
                nam -= k
                if nam == 0:
                    print('다 팔렸어요~')
                    fruitlist[i]['count']=nam
                    profit = profit + (int(fruitlist[i]['price'])-int(fruitlist[i]['cost']))*k
                    pan = pan+k
                elif nam < 0:
                    s=fruitlist[i]['count']
                    print(f'재고보다 많이 팔 수는 없어요~~! 현재재고는 {s}개 입니다.')                     
                else:
                    fruitlist[i]['count']=nam
                    profit = profit + (int(fruitlist[i]['price'])-int(fruitlist[i]['cost']))*k
                    pan = pan+k
                break
        print(f'누적 수익은 {profit}원이고 누적 판매량은 {pan}개입니다.')
        break
    return profit,pan

def fruit_list(fruitlist,profit):
    print('--------------------------  재고리스트  ----------------------------')
    print(*fruitlist,sep='\n')
    print('--------------------------------------------------------------------')
    print(f'누적 수익은 {profit}원 입니다.')
        
def fruit_del(fruitlist):
    print('--------------------------  재고리스트  ----------------------------')
    print(*fruitlist,sep='\n')
    print('--------------------------------------------------------------------')
    choice1 = input('삭제하려는 과일명을 입력하세요 >>> ')
    delok = 0
    for i in range(len(fruitlist)):
        if fruitlist[i]['name'] == choice1:
            print('삭제되었습니다.')
            del fruitlist[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 과일입니다.')
    print('--------------------------  재고리스트  ----------------------------')
    print(*fruitlist,sep='\n')
    print('--------------------------------------------------------------------')