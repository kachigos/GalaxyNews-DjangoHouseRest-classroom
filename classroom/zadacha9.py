a = int(input())
years = int(input())
def bank(a, years):
    summ = a
    for i in range(years):
        summ += (a * 0.1)
    return summ
print(bank(a, years))