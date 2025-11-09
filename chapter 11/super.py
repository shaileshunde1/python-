# basically allowing the other constructors to also execute
# to use super class constructor in derived class

class employee:
    def __init__(self,company):
        company  =  "Microsoft"

class programmer(employee):
    def init(self):
        super().__init__()

    