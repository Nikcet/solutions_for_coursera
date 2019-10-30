import math
a, b, c = float(input()), float(input()), float(input())
P = (a + b + c) / 2
S = math.sqrt(P * (P - a) * (P - b) * (P - c))
print(S)
