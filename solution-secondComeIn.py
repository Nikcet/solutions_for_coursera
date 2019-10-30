s = input()
i = 0

pos1 = s.find('f')
pos2 = s.find('f', pos1 + 1)

if pos1 > -1:
    i = i + 1

if pos2 > -1:
    i = i + 1
    print(pos2)

if i == 1:
    print(-1)
elif i == 0:
    print(-2)
