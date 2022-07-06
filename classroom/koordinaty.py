x = float(input('number for x:'))
y = float(input('number for y:'))
a = 'I'
b = 'II'
c = 'III'
d = 'IV'
if x != 0 and y != 0:
    if x * y > 0 and x >0:
        print('I')
if x < 0 and y > 0: 
    if x * y < 0:
	print('II')
if x < 0 and y < 0:
    if x * y > 0:
	print('III')
if x > 0 and y < 0:
    if x * y < 0:
	print('IV')
