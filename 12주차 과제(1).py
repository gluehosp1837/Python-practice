with open("prime_numbers.txt", "r")as file:
    contents = file.read()
numbers = contents.split(', ')
List_numbers = list(map(int, numbers))

#출력 처리 위해 설정
List_numbers_fact = map(str, List_numbers)
List_numbers_fact = str.join('! ', List_numbers_fact)

#리스트 자료형 하나하나 불러내서 factorial 사용
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = len(List_numbers)
ans = 0
for i in range(num):
    ans += factorial(List_numbers[i])
print(List_numbers_fact, end='!')
print(' =', ans)