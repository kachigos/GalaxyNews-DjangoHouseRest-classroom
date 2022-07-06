class Phone:
    def __init__(self, model, number, weight):
        self.number = number
        self.model = model
        self.wieght = weight

    def op(self):
        print(f'Телефон модель {self.model} номер телефона тут {self.number}, вес тут {self.wieght}')

    def send_message(self, *args):
        for i in args:
            print(i)


xioami = Phone('Xiaomi', 5555431412, '100g')
sumsung = Phone('Sumsung', 3455431412, '200g')
lg = Phone('Lg', 1235431412, '150g')

xioami.op()
sumsung.op()
lg.op()
xioami.send_message(1231334, 34123235, 64145646, 7344326)
sumsung.send_message(1231334, 34123235, 641231246, 7344326)
lg.send_message(1231334, 34123235, 641451231236, 734412326)