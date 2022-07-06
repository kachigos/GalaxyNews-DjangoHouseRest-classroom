for d in range(10):
    a = int(input('chislo ot 2 do 9:'))
    b = int(input('chislo ot 2 do 9:'))
    c = int(input('your answer: '))
    x = a * b
    if x == c:
        print(' true ')
    elif c != x:
        print('False, correct answer:', x)
    else:
        print('try')