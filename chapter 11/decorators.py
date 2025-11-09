#used when we need to use anything irrespective of situation

@staticmethod #used to tell that class doesnt need an object
def greet():
    print("Goodmorning")

# ----------------------------------------------------------
class employee:
    a =  2


    @classmethod # used to give class atribute preference over instance 
    def show(cls):
        print(f"The class atrribute is {cls.a}")
    

b = employee()
b.a = 45
b.show()

# ----------------------------------------------------------
@property 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2


# ----------------------------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
        
#used so that no invalid values are used 
