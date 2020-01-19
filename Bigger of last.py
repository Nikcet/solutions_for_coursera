# Дан список чисел. 
# Выведите все элементы списка, которые больше предыдущего элемента.

# Получаем список
numList = [int(i) for i in input().split()]
nextNum = numList[0]
lastNum = numList[0]

# Перебираем каждый элемент списка, начиная со 2-го
for i in range(1, len(numList)):
    lastNum = numList[i-1]
    nextNum = numList[i]
    if nextNum > lastNum:
        print(nextNum)
