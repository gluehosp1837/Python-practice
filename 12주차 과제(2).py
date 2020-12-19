num1 = int(input('Input start number ? '))
num2 = int(input('Input number count ? '))

a = []
for i in range (num1, 10000):
    c = 0
    if len(a) == num2:
        break

    for j in range(2, i):
        if i%j == 0:
            c = 1
            break
    if c == 0:
        a.append(i)

a_str = map(str, a)
a_str = str.join(', ', a_str)

with open("prime_numbers.txt", "w")as file:
    file.write(a_str)
print(a_str)