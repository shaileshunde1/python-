#code to store employee info in a class of microsoft

class programmer:
    company ="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name  = name
        self.salary  = salary
        self.pincode  = pincode

        
p = programmer("Harry", 1200000, 421306)
print(p.name,p.salary,p.pincode,p.company)