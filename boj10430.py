a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

2 <= a
c <= 10000

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
