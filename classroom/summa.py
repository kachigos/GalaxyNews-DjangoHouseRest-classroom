n = input("numbers: ")
 
suma = 0
mult = 1
 
for x in n:
    if x.isdigit():
        suma += int(x)
 
print("summa: ", suma)
