word = input().upper() #전부 대문자

word_list = list(set(word))
count_list = []

for i in word_list:
    count = word.count(i)
    count_list.append(count)

if count_list.count(max(count_list))>1:
    print('?')
else:
    print(word_list[count_list.index(max(count_list))])
print()