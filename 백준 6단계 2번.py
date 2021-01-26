def d(n):
    result = n
    while True:
        num = n % 10
        result = result + num
        n = int(n / 10)
        if n == 0:
            break
    return result

a = [0 for i in range(10001)]
a[0] = 1

for i in range(0, 10001):
    if a[i] != 0:
        i = i+1
    elif a[i] == 0:
        j = i
        while True:
            j = d(j)
            if j > 10000:
                break
            a[j] = a[j] + 1

for k in range(0, 10001):
    if a[k] == 0:
        print(k)