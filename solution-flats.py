x = int(input())
y = int(input())

flatsPerPorch = y - x + 1

if (x - 1) % flatsPerPorch == 0:
    print("YES")
else:
    print("NO")
