a = input( "File: ")
if '.' in a:
    print(a[a.rfind('.')+1:])
else:
    print('Error')
