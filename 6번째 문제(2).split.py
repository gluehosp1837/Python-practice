#사용자 입력을 받아 문자, 숫자 구분:try-except 구문 사용
x = input().split(" ")
y = []

for word in x:
    try:
        int(word)
        y.append(word)
        x.insert(x.index(word), 'X')
        x.remove(word)
    except:
        y.append('X')
        print('예외발생')
    else:
        print('정상작동')

print(x)
print(y)