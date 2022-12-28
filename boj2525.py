lst = list(input().split())
C = int(input())

A = int(lst[0])
B = int(lst[1])

if C >= 60:
    D = C//60
    E = C%60

    Hr = A + D
    Mn = B + E

    if Mn >= 60:
        Mn = Mn - 60
        Hr = Hr + 1

else:
    Hr = A
    Mn = B + C

    if Mn >=60:
        Mn = Mn - 60
        Hr = Hr + 1


if Hr >= 24:
    Hr = Hr - 24

print("{} {}".format(Hr, Mn))