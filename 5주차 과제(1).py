Number1 = input('Input Number 1 ? ')
Number2 = input('Input Number 2 ? ')
Number3 = input('Input Number 3 ? ')

if Number1 > Number2 > Number3:
    print('Max number is', Number1)
    print('Min number is', Number3)

elif Number1 > Number3 > Number2:
    print('Max number is', Number1)
    print('Min number is', Number2)

elif Number2 > Number1 > Number3:
    print('Max number is', Number2)
    print('Min number is', Number3)

elif Number2 > Number3 > Number1:
    print('Max number is', Number2)
    print('Min number is', Number1)

elif Number3 > Number1 > Number2:
    print('Max number is', Number3)
    print('Min number is', Number2)

else:
    print('Max number is', Number3)
    print('Min number is', Number1)