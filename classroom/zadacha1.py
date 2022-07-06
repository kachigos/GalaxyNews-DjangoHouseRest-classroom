t = 'The Zen of python c C '

for i in t.split():
    if i.startswith("C"):
        print(i)
    if i.startswith("c"):
        print(i)