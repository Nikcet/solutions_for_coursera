hh1 = int(input())
mm1 = int(input())
ss1 = int(input())

hh2 = int(input())
mm2 = int(input())
ss2 = int(input())

ss1 = ss1 % 60
mm1 = mm1 % 60
hh1 = hh1 % 24

ss2 = ss2 % 60
mm2 = mm2 % 60
hh2 = hh2 % 24

S1 = ss1 + mm1 * 60 + hh1 * 3600
S2 = ss2 + mm2 * 60 + hh2 * 3600

if S1 > S2:
    dif = S1 - S2
    dif = str(dif)
else:
    dif = S2 - S1
    dif = str(dif)

print(dif)
