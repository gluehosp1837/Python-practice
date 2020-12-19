#파일 읽기
file = open('result.txt', 'r')
cnt = 0

for line in file:
    print(line)
    cnt += 1

print(cnt)
file.close()