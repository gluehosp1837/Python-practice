#반복문 써서 숫자 나열, 출력되는 수가 홀수면 -> 1, 짝수면 -> 0으로 변환
x = int(input())
a = list(range(1, x+1))

file = open('result.txt', 'w')

def Isodd(num):
    if num % 2 == 0:
        return 0
    else:
        return 1

output = map(Isodd, a)

for i in output:
    print(i)
    file.write(str(i)+'\n')
    
file.close()