i = input('programming language:')
e = int(input('how old are you:'))
print(end = '')
o = int(input('work experience:'))
s = int(input('wish salary:'))
a = 'java'
b = 'javascript'
c = 'python'
if i == a or i == b or i == c and 18 <= e < 60 and o > 3 and s <= 60000:
    print('you are hired')
else:
    print('Error')
