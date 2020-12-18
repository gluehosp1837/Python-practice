num = int(input('Input number ? '))

def prime(num):
    prime_list = []
    for i in range(2, num+1):
        n = 0
        for j in range(1, i):
            if i%j == 0:
                 n = n + 1
        if n == 1:
                prime_list.append(i)
    a = max(prime_list)

    return a

print('Max prime number =', prime(num))
