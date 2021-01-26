num = []

for i in range(10):
    a = int(input())
    b = a%42
    num.append(b)
print(len(set(num)))