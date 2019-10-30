A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A > 8:
    A = A // 8
else:
    A = A

if B > 8:
    B = B // 8
else:
    B = B

if C > 8:
    C = C // 8
else:
    C = C

if D > 8:
    D = D // 8
else:
    D = D

if C - A == 1 or C - A == 0 or C - A == -1 and \
        D - B == 1 or D - B == 0 or D - B == -1:
    print("YES")
else:
    print("NO")
