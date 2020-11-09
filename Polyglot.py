# Каждый из N школьников некоторой школы знает Mᵢ языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

# Формат ввода
# Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих названия языков, которые знает i-й школьник. Длина названий языков не превышает 1000 символов, количество различных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.

# Формат вывода
# В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.

# Доработанное готовое решение
students = [{input() for j in range(int(input()))}
            for i in range(int(input()))]
known_by_everyone = set.intersection(*students)
known_by_someone = set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')

# Мое решение в лоб
knowAllStudents = set()
knowAllLanguages = set()

for i in range(int(input())):
    lang = set()
    for j in range(int(input())):
        lang.add(input())
        knowAllLanguages |= lang
        knowAllStudents |= lang
    knowAllStudents &= lang

print(len(knowAllStudents))
for i in knowAllStudents:
    print(i)

print(len(knowAllLanguages))
for i in knowAllLanguages:
    print(i)