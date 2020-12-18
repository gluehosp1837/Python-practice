def multiply(a, b):
    if b > 0:
        return a + multiply(a, b-1)
    else:
        return 0

a = int(input('Input number1 ? '))
b = int(input('Input number2 ? '))

print('{}*{}={}'.format(a, b, multiply(a, b)))
