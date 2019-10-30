def sum(a, b):
    if b != 0:
        return sum(a + 1, b - 1)
    print(a)


a, b = int(input()), int(input())
sum(a, b)
