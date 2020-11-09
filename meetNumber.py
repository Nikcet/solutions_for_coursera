N = list(map(int, input().split()))
numbers = set()

for i in N:
    if i in numbers:
        print("YES")
    else:
        print("NO")
        numbers.add(i)
