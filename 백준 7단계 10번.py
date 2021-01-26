cnt = 0
for i in range(int(input())):
    word = input()
    cnt+=list(word) == sorted(word, key=word.find)
print(cnt)