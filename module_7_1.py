class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        new_str = f'{self.name}, {self.weight}, {self.category}'
        return new_str


class Shop:
    _file_name = 'products.txt'

    def get_products(self):
        file = open(self._file_name, 'r', encoding="utf-8")
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        file = open(self._file_name, 'r+', encoding="utf-8")
        text = file.read()
        for i in products:
            if i.name in text:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file.write(str(i) + '\n')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
