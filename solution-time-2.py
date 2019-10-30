N = int(input())
ss = N % 86400
mm = ss // 60
hh = ss // 3600

ss = ss % 60
mm = mm % 60
hh = hh % 24

if ss < 10:
    ss = str(0) + str(ss)
else:
    ss = str(ss)
if mm < 10:
    mm = str(0) + str(mm)
else:
    mm = str(mm)

ss = str(ss)
mm = str(mm)
hh = str(hh)

print(hh + ':' + mm + ':' + ss)
