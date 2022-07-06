def spisok(list1):
    po1 = []
    otr = []
    for i in list1:
        if i >= 0:
            po1.append(i)
        else:
            otr.append(i)
    return po1, otr
a = int(input())
list1 = []
for i in range(a):
    f = int(input())
    list1.append(f)
print(spisok(list1))