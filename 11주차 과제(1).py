num1 = int(input('Input number 1 ? '))
num2 = int(input('Input number 2 ? '))

def factorial(num):
    fact_value = 1
    for i in range(1, num+1):
        fact_value *= i
    return fact_value

sum_value = 0
for i in range(num1, num2+1):
    sum_value += 1/factorial(i)
    if i == num2:
        print('1/{}! ='.format(i), end=' ')
    else:
        print('1/{}! +'.format(i), end=' ')
print(sum_value)