a = int(input())
b = int(input())

ans1 = a*(b%10)
ans2 = a*((b//10)%10)
ans3 = a*(b//100)
total = a*b

print(ans1)
print(ans2)
print(ans3)
print(total)