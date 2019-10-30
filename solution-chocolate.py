n = int(input())
m = int(input())
k = int(input())

s = m * n
if s >= k:
    if s % 2 == 0 and k % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
