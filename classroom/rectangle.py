class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimetr(self):
        return f"Периметр прямоугольника: {(self.length + self.width) * 2}"

    def square(self):
        return f"Площадь прямоугольника: {self.length * self.width}"


def main():
    a, b = map(int, input("Введите длину и ширину через пробел: ").split())
    rectangle = Rectangle(a, b)
    while True:
        choose = int(input("1. Найти периметр прямоугольника.\n2. Найти площадь прямоугольника.\n3. Выход.\n  >>>"))
        if choose == 1:
            print(rectangle.perimetr())
        elif choose == 2:
            print(rectangle.square())
        elif choose == 3:
            break
        else:
            print("Ошибка")
            break


main()