#첫 숫자 random, 증가범위 random, ? target random
#random한 첫 수를 증가범위에 맞춰 리스트에 5개 삽입한 뒤, 받은 target의 index를 저장해서 출력할때 그 target의 숫자만 ?로 바뀌게 출력
#?로 가려진 숫자가 사용자가 입력한 숫자랑 같으면 correct, 틀리면 wrong, 답은 얼마다라고 이야기 해줌
import random

a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 4)
d = []

d.append(a)
if b != 0:
    for a in range(a, 50, b):
        a += b
        d.append(a)
        if len(d) == 5:
            break
else:
    while True:
        a == a
        d.append(a)
        if len(d) == 5:
            break

e = d[c]
del d[c]
d.insert(c,'?')

print(d)
f = int(input('Input Number ? '))

if e == f:
    print('correct')
else:
    print('wrong, answer = {}'.format(e))