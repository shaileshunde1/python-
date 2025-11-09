class animals:
    pass

class pets(animals):
    pass

class dogs(pets):
    @staticmethod
    def bark():
        print("Bow bow")

d = dogs()
d.bark()