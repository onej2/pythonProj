# pip install cx_Oracle
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

cursor.execute("select * from emp where deptno = 10")
print(cursor)

for item in cursor:
    print(item[1],item[5])

    print(item)

conn.close()

# while True:
#     choice=input('''
# 다음 중에서 하실 일을 골라주세요 :
# 1. job 검색  2. name 검색  3. 종료
# >>> ''')
#     if choice == '1':
#         jo = input('job을 입력하세요 >>> ').upper()
#         cursor.execute(f"select * from emp where job = '{jo}' ")
#         for item in cursor:
#             print(item[1:8])
            
#     elif choice == '2':
#         na = input('name의 일부를 입력하세요 >>> ').upper()
#         cursor.execute(f"select * from emp where ename like '%{na}%' ")
#         for item in cursor:
#             print(item[1:8])   
        
#     elif choice == '3':
#         break
    


