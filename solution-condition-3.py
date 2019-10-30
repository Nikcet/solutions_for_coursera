A = int(input())
B = int(input())
C = int(input())

if A >= B and A >= C:
    number = A
elif A <= B and B >= C:
    number = B
else:
    number = C

print(number)
