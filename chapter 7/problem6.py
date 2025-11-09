#code to calculate the factorial 

n=int(input("Enter your number: "))
factorial = 1

for i in range(1,n+1):
    factorial = factorial * i


print(f"The factorial of {n} is {factorial}")