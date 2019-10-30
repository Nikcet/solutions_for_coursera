v = int(input())
t = int(input())
S = 109
s = 0
if v > 0:
    s = v * t
else:
    s = 109 - (-v * t)
s = s % 109
print(s)
