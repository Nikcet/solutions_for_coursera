s = input()
i = 0

pos1 = s.find('f')
if pos1 > -1:
    i = i + 1

pos2 = s.find('f', pos1 + 1)
if pos2 > -1:
    i = i + 1

if i >= 2:
    pos3 = s.rfind('f', pos2)
    if pos3 > -1:
        print(pos1, pos3)
elif pos1 != -1:
    print(pos1)
