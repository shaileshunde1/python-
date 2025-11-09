#write a  class train to book tickets,get status and fare info

from random import randint

class train:
    def __init__(self, trainNO):
        self.trainNo =trainNO

    def book(self,fro, to):
        print(f"Train {self.trainNo} is booked successfully from {fro} to {to}")
        
    def getstatus(self):
        print(f"Train {self.trainNo} is running on time")

    def fare(self):
        print(f"Fare for your booking {randint(222,5555)}")

    @staticmethod
    def greet():
        print("Gummorning mr president")

    
s = train(12399)
s.greet()
s.book("delhi", "mumbai")
s.getstatus()
s.fare()

#multiple errors but finally did it 