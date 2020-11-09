# Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ею чисел есть задуманное или NO в противном случае. После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.

# Формат ввода

# Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных пробелами. После каждой строки с вопросом идет ответ Августа: YES или NO. Наконец, последняя строка входных данных содержит одно слово HELP.

# Формат вывода

# Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.

sumSet = set(map(str, range(1, int(input()) + 1)))

while True:
    nums_set = set(map(str, input().split()))
    if "HELP" in nums_set:
        break
    ans = input()
    if "HELP" in ans:
        break
    elif "YES" in ans:
        sumSet &= nums_set
    elif "NO" in ans:
        sumSet -= nums_set

sumList = list(sumSet)
for i in range(len(sumList)):
    sumList[i] = int(sumList[i])
print(*sorted(sumList))
