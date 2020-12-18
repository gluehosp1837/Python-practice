#입력받은 수를 띄워서 정렬할 것, 재귀함수 사용
num = int(input('Input number ? '))

def function(num):
    a = []
    if num < 10:
        a.append(num)
    else:
        a.append(num%10)
        a.append(function(num//10))
    return a
#입력 받은 수를 분리 시켜줌, 중첩 리스트문으로 출력됨

array = function(num)

def flatten(array):
    b = []
    for i in array:
        if type(i) == type(list()):
            b+=(flatten(i))
        else:
            b.append(i)
    return b
#중첩 리스트로 출력된 값을 flat하게 변환시켜줌

Data = list(reversed(flatten(array)))
Data = map(str, Data)
print(' '.join(Data))