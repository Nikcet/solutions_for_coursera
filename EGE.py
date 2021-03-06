# Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ, 
# каждый из них оценивается целым числом от 0 до 100 баллов. 
# При этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку) по любому экзамену из конкурса выбывают. 
# Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.

# В конкурсе участвует N человек, при этом количество мест равно K. 
# Определите проходной балл, то есть такое количество баллов, что количество участников, 
# набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов, 
# набравших наибольшее количество баллов среди непринятых абитуриентов, 
# общее число принятых абитуриентов станет больше K.

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
# Считываем кол-во проходных мест из файла
K = int(inFile.readline())
listGoodPoints = []

# Обходим весь список студентов, отсекаем не проходящих по баллам, 
# суммируем баллы проходящих и вкладываем в список суммированных баллов
for line in inFile:
    listPoints = line.split()
    if ((int(listPoints[-1]) > 39 and int(listPoints[-2]) > 39 and
            int(listPoints[-3]) > 39)):
        (listGoodPoints.append(int(listPoints[-1]) +
         int(listPoints[-2]) + int(listPoints[-3])))

inFile.close()
# Сортируем список суммированных баллов по убыванию
listGoodPoints.sort(reverse=True)

# Находим проходной балл
def contest(k, listScores):
    # Если зачисляются все студенты, не имеющие неудовлетворительных оценок
    if (len(listScores) <= k):
        return 0
    # Если кол-во студентов, у которых равный максимальный балл больше, чем кол-во проходных мест (K)
    # (если первый элемент(самый большой) в списке равен K-тому)
    elif listScores[0] == listScores[K]:
        return 1
    for i in range(k, 0, -1):
        # Обходим список баллов с конца, если текущий элемент меньше предыдущего, 
        # то выводим предыдущий балл как проходной
        if listScores[i] < listScores[i - 1]:
            return listScores[i - 1]


print(contest(K, listGoodPoints), file=outFile)
outFile.close()
