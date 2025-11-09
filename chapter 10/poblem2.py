# #code to create class calc capable of finding square,cube,sqr root

class calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square is {self.n*self.n}")
    
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    
    def root(self):
        print(f"The squareroot is {self.n**1/2}")
    
    @staticmethod
    def greet():
        print("Goodmorning Shemnya")


a = calculator(5)
a.greet()
a.square()
a.cube()
a.root()



# class calculator:
#     def __init__(self,n):
#         self.n  =  n

#     def square(self):
#         print(f"The square is {self.n*self.n}")
        

# a =  calculator(5)
# a.square()