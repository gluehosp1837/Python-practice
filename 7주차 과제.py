for i in range(1, 10):
    for j in range(2, 10):
        if (i*j)%2 == 1:
            print('{}x{}={:2}'.format(j, i, '*'), end=" ")
        else:
            print('{}x{}={:2}'.format(j, i, i*j), end=" ")
    print()
