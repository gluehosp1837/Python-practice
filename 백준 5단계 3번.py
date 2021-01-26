num = []

A = int(input())
B = int(input())
C = int(input())

tot = str(A * B * C)

for i in tot:
    num.append(i)

for i in range(10):
    print(num.count(str(i)))