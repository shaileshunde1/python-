class Employee:
    job = "Salesman"
    language = "english"
    salary = 1200000

#def init is a constructor and yea thats about it
#also called as dunder method which is called automatically after creating object
# __init__ is a constructor: it is needed to give identical values ahead otherwise
#all the employees will have the same values of language,job,salary

    def __init__(self,name,salary,job,language):
        self.name = name
        self.salary = salary
        self.job = job
        self.language = language

    def getinfo(self):
        print(f"employee job is {self.job} and language is {self.language} with {self.salary}")

    @staticmethod #this tells the system that this doesnt need a object
    def greet():
        print("Good morning")



shailesh = Employee("skrillex", 1500000,"developer", "python")

shailesh.greet()
shailesh.getinfo()
print(shailesh.name,shailesh.language,shailesh.job,shailesh.salary)




    