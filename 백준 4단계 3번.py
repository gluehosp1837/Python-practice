a = b = int(input())
c = 0

while True:
    ten = a//10
    one = a%10
    total = ten + one
    c = c+1
    a = int(str(a%10)+str(total%10))
    if (b == a):
        break
print(c)