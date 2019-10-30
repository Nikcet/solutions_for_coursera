s = input()

pos1 = s.find('h')
pos2 = s.rfind('h', pos1)

if pos1 != -1 and pos2 != -1:
    pos3 = s[pos1:pos2 + 1]
    if pos3 != -1:
        pos = s.replace(pos3, '')
        print(pos)
