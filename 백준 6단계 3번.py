def hansu(val):
    if val < 100:
        return True
    D = list(map(int, str(val)))
    leng = len(D)
    result = D[0] - D[1]
    for i in range(leng - 1):
        tmp = D[i] - D[i + 1]
        if result != tmp:
            return False
    return True

N = int(input())
cnt = 0
for i in range(1, N+1):
    if hansu(i):
       cnt += 1

print(cnt)