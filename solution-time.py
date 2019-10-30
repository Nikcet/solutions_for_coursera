N = int(input())

N = N % 1440
hours = N // 60
minutes = N % 60

print(hours, minutes)
