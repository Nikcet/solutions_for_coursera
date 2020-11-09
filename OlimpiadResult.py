# В олимпиаде участвовало N человек. 
# Каждый получил определенное количество баллов, при этом оказалось, 
# что у всех участников разное число баллов. 
# Упорядочите список участников олимпиады в порядке 
# убывания набранных баллов.

class Olimpiad:
    points = 0
    name = ''

N = int(input())
peopleList = []
# В цикле принимаем список учащихся и их баллы. 
# Раскладываем баллы и фамилии по отдельным полям. 
for i in range(N):
    studentsList = input().split()
    students = Olimpiad()
    students.points = int(studentsList[1])
    students.name = studentsList[0]
    # Вставляем в список имеющуюся структуру для последующей сортировки по баллам.
    peopleList.append(students)
# Сортируем список по баллам.
peopleList.sort(key=lambda olimpiad: (-olimpiad.points, olimpiad.name))
# Последовательно выводим имена из структуры.
for students in peopleList:
    print(students.name)
