a = int(input('number:'))
b = int(input('number:'))
c = int(input('number:'))
if a < b and a < c:
    print('min:', a)
if b < a and b < c:
    print('min:',b)
if c < a and c < b:
    print('min:', c)
if a > b and a > c:
    print('max:', a)
if b > a and b > c:
    print('max:', b)
if c > a and c > b:
    print('max:', c)
