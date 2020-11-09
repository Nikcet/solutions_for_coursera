inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
datas = []

for line in inFile:
    datas.append(line.split())

datas.sort(key=lambda x: x[0])

for line in datas:
    print(line[0], line[1], line[3], file=outFile)

inFile.close()
outFile.close()
