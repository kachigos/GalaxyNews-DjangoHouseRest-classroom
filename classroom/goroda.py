print ("""
Выберите действие:
1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход
    """
    )


choice = int(input('Выберите число:'))
cities = ('Bishkek')
if choice == 1:
    new_city = input("Название нового города:")
    if  new_city:
        print("Неверное название")
    elif new_city in cities:
        print("Такой город уже есть")
    else:
        cities.append(new_city)    
