class Mahsulot:
    def __init__(self, nom):
        self.nom = nom


class Savat:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item.nom)

    def show(self):
        print(self.items)


m1 = Mahsulot("Olma")
m2 = Mahsulot("Banan")

s1 = Savat()
s1.add_item(m1)
s1.add_item(m2)
s1.show()
