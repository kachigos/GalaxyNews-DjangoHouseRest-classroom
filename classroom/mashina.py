m = 'лексус'
y = '2005'
p = '150000'
c = 'белый'
s = 'правый руль'
h = 1
i = 10000 #цена
if m == 'лексус' or m == 'тайота' and p == 150000 and c =='белый' or c == 'серый' and h  <= 2 and s == 'правый руль' and i <= 10000:
    print(True)
if m == 'лексус' or m == 'тайота' and p == 200000 and c == 'серый' and h <= 2 and s and s == 'правый руль' and i <= 8000:
    print(True)
else:
    print(False)