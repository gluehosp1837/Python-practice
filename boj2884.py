h,m = input().split()

h = int(h)
m = int(m)

if m >= 45:
    print(h, m-45)
elif m < 45:
    if h == 0:
        print(h+23, m+15)
    else:
        print(h-1, m+15)
