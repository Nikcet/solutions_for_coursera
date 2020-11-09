import sys 
# K - кол-во мест
K = int(input())
studentsList = open('input.txt', 'r', encoding='utf8')
output = open('output.txt', 'w', encoding='utf8')
sumsList = []
answer = 0
N = 0

for line in studentsList:
    N += 1

if N != 0:
    for line in studentsList:
        subject_1 = int(line.split()[-1])
        subject_2 = int(line.split()[-2])
        subject_3 = int(line.split()[-3])
        if subject_1 > 39 and subject_2 > 39 and subject_3 > 39:
            sumsList.append(subject_1 + subject_2 + subject_3)
            N -= 1
        if N == 0 or K == 0:
            print(0, file=output)
            studentsList.close()
            output.close()
            sys.exit
else:
    print(1, file=output)
    studentsList.close()
    output.close()
    sys.exit

studentsList.close()

newSumsList = [0] * 301

for i in sumsList:
    newSumsList[i] += 1

for i in range(len(newSumsList)):
    if newSumsList[i] > 0 and K > 0 and newSumsList[i] < K:
        K -= newSumsList[i]
    elif newSumsList[i] > K:
        answer = i
        break

print(answer, file=output)

output.close()