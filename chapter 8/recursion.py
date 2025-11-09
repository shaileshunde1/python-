# factorial(0)=1
# factorial(1)=1
# factorial(2)=2x1

#factorial(n) = n * factorial(n-1) - basic logic

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n= int(input("Enter your number: "))
print(f"The factorial of {n} is: {factorial(n)}")