A = int(input())
B = int(input())
C = int(input())


if A > B:
    number = A
else:
    number = B

if B > C:
    number = B
else:
    number = C
if A > C:
    number = A
else:
    number = C

print(number)
