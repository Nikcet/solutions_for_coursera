inFile = set(open('input.txt', 'r', encoding='utf8').readlines())
array = set()

for line in inFile:
    array = array | set(line.split())

print(len(array))
