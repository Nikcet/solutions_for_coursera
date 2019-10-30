def sums(a):
    a = int(input())
    if a != 0:
        return a + sums(a)
    else:
        return a


a = 0
print(sums(a))
