import func
print('연산의 달인 게임 시작')

for i in range(1, 11):
    n1, n2, op = func.ques()
    func.numb(n1, n2, op)
    user, res = func.show(op, n1, n2, i)
    func.chec(res, user)

print('연산의 달인 게임 종료')