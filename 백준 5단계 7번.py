testnum = int(input())

for i in range(testnum):
    testcase = list(map(int, input().split()))
    average = sum(testcase[1:])/testcase[0]
    studentsnum = 0
    for j in testcase[1:]:
        if j > average:
            studentsnum += 1
    print(str('%.3f'%round(studentsnum/testcase[0]*100, 3)) + '%')