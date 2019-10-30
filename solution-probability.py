import random
from collections import Counter
a = 30
b = 15
c = 5
d = 30
e = 20

P = a+b+c+d+e
Counter(random.choices(["a", "b", "c", "d", "e"], weights=[30, 15, 5, 30, 20])[0]
    for i in range(100))
