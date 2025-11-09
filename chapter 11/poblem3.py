#create a class employee and add salary and increment propert

class employee:
    salary = 20000
    increment = 20

    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryafterincrement.setter
    def salaryAfterIncrement(self, salary):
     self.increment = ((salary/self.salary) - 1) * 100


e = employee()
print(f"Increment is {e.increment} %")