a = int(input('1st number:'))
b = int(input('2nd number:'))
c = int(input('your answer: '))
x = a * b
if x == c:
    print (' true ')
elif c != x: 
    print('False, correct answer:', x)
else:
    print('try')
