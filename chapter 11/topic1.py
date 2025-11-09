#Inheritance is a way of using an old class in a new class


#single inheritance
class company:
    company  =  "Microsoft"

    def __init__(self):
        print(f"The name of the company is {self.company}")

class programmer(company):
    def printer(self):
        print(f"The programmer is from {self.company}")
    

a = company()
b =programmer()

b.printer()

#similary if you take 2 classes into 1 class then its multiple inheritance


#multilevel inheritance
class employee:
    a = 1

class mastikhor(employee):
    b = 2

class kaamchor(mastikhor):
    c = 3

o = kaamchor
print(o.a, o.b, o.c)