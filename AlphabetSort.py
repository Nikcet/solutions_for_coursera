#  В олимпиаде по информатике принимало участие несколько человек.
# Определите и выведите средние баллы участников олимпиады 
# в 9 классе, в 10 классе, в 11 классе. Данные брать из файла, записывать результат в другой файл. 
inFile = open('input.txt', 'r', encoding='utf8') # Открываем файл для чтения
outFile = open('output.txt', 'w', encoding='utf8') # Открываем файл для записи
datas = []
middle9, middle10, middle11 = 0, 0, 0
count9, count10, count11 = 0, 0, 0
# Перебором разбиваем все данные из файла "input.txt" и распределяем, 
# не сохраняя информацию из самого файла в памяти компьютера.
for line in inFile:
    datas = line.split()[2:4]
    if int(datas[0]) == 9:
        middle9 += int(datas[1])
        count9 += 1
    elif int(datas[0]) == 10:
        middle10 += int(datas[1])
        count10 += 1
    elif int(datas[0]) == 11:
        middle11 += int(datas[1])
        count11 += 1
# Считаем среднее арифметическое полученных данных
answer9, answer10, anser11 = \
    middle9/count9, middle10/count10, middle11/count11

print(answer9, answer10, anser11, file=outFile)
# Закрываем файлы 
inFile.close()
outFile.close()
