testnum = int(input())

for i in range(testnum):
    testcase = input()
    sum = 0
    score = 0
    for j in testcase:
        if j == 'O':
            score += 1
        else : 
            score = 0
        sum += score
    print(sum)