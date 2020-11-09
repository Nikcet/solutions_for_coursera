Num = 1
while Num != 0:
    Num = int(input())
    for i in range(1, Num):
        if Num % i == 0:
            print(Num // i)

n = int(input())

verFirst = 1 / n
verSecond = 2 / (n - 1)

answer = (verFirst + verSecond) - (verFirst * verSecond)
standard = 1 / 31

print(standard * 100, answer * 100)
