# Штаб гражданской обороны Тридесятой области решил обновить план 
# спасения на случай ядерной атаки. 
# Известно, что все n селений Тридесятой области находятся вдоль 
# одной прямой дороги. Вдоль дороги также расположены m бомбоубежищ, 
# в которых жители селений могут укрыться на случай ядерной атаки.
# Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее, 
# необходимо для каждого селения определить ближайшее к нему бомбоубежище.

n = int(input()) #Кол-во селений
town = list(enumerate(map(int, input().split()))) #Расстояние от начала дороги до селений
m = int(input()) #Кол-во бомбоубежищ
bomba = list(enumerate(map(int, input().split()))) #Расстояние от начала дороги до бомбоубежищ
indexBomb = 0
answer = []

# Функция для сортировки кортежей по 2-му элементу
def SecondElem(item):
    return item[1]

# Сортировка списка кортежей по второму элементу кортежа (значению)
town.sort(key=SecondElem)
bomba.sort(key=SecondElem)
# Вся магия. Перебор значений и сравнение их друг с другом.
for indexTown in range(n):
    townElem = town[indexTown]
    while indexBomb != m - 1 and abs(townElem[1] - bomba[indexBomb][1]) > \
            abs(townElem[1] - bomba[indexBomb + 1][1]):
        indexBomb += 1
    else:
        answer.append([bomba[indexBomb][0]+1, town[indexTown][0]])
# Сортировка полученных данных по второму элементу кортежа (индексу)
answer.sort(key=SecondElem)
print(*[indexAnswer[0] for indexAnswer in answer])
