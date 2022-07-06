n1 = int(input("введите целое цисло: "))
n2 = 0 
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10 
    n2 = n2 * 10
    n2 = n2 + digit
print ("обратное число: ",n2)
