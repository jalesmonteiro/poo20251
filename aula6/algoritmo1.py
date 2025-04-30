class Pai:
    def __init__(self, p1):
        self.p1 = p1

    def metodo1(self):
        print("pai - metodo 1")

    def metodo2(self):
        print("pai - metodo 2")

class Filha1(Pai):
    def metodo2(self):
        print("filha 1 - metodo 2")

class Filha2(Pai):
    def __init__(self, p1, p2):
        super().__init__(p1)
        self.p2 = p2

    def metodo2(self):
        print("filha 2 - metodo 2")

obj1 = Pai(1)
obj2 = Filha1(2)
obj3 = Filha2(3, 3)

obj1.metodo1()
obj1.metodo2()
obj2.metodo1()
obj2.metodo2()
obj3.metodo1()
obj3.metodo2()