import math
import random
import timeit

start = timeit.default_timer()

x = input('로또를 통해 일확 천금을 노리자!(1 ~ 45 사이의 숫자 6개 입력)').split(' ')
x = list(map(int, x))
x.sort()

y = []
cnt = 1
while x != y:
    y.clear()
    while len(y) != 6 :
        a = int(random.randrange(1, 46))
        if a in y:
            continue
        else:
            y.append(int(a))
        y.sort()
        cnt += 1

end = timeit.default_timer()
b = (end - start)

print('내가 뽑은 숫자 : ',x)
print('당첨번호 : ',y)
print(cnt,'번째에 당첨했습니다. 총',1000*cnt,'원을 쓰시고 당첨되셨네요.')
print(b)