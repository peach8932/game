
import random
# 함수 정의

# 문제만들기 기능
def ques():
    n1 = random.randrange(1, 100)
    # 두자리 수가 랜덤
    n2 = random.randrange(1, 10)
    op_list = ['+', '-', '*', '/']
    op = random.choice(op_list)
    # print(n1, op, n2)
    return n1, n2, op 

# 문제 앞뒤 변경
def numb(n1, n2, op):
    if op == '-' or op == '/':
        print('두수 바꿈')
        # 두수 바꿈 만들어 보세요
        #큰 값 저장기능
        front = max(n1,n2)
        #작은 값 저장기능 
        back = min(n1,n2)
        #두 수를 변경
        n1 = front 
        n2 = back 

# 문제 출력 기능
def show(op, n1, n2, i):
    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1 - n2
    elif op == '*':
        res = n1 * n2 
    elif op == '/':
        res = n1 / n2

    user = int(input(f'{i}문제 {n1} {op} {n2} = ' ))
    return user, res

# 답 체크
def chec(res, user):
    if user == res:
        print('정답! 계속합니다.')
    else:
        print('땡~ 틀렸습니다.')
        

ques()