def divide(a, b):
    quotient = 0
    a = abs(a)
    b = abs(b)

    while(a >= b):
        a = a-b
        quotient += 1
    return quotient

a = int(input('Input number 1 ? '))
b = int(input('Input number 2 ? '))

print('{}/{}={}'.format(a, b, divide(a, b)))
