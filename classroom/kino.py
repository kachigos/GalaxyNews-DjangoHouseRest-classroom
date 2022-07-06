j = input('Type:')
t = input('Time:')
if j == 'thriller' or j == 'comedy'or j == 'detective' and 8 <= t < 21:
    print('It costs 300')
elif j == 'thiller' or j == 'comedy' or j == 'detective' and 21 <= t < 24:
    print('It costs 500')
else:
    print('Error')
