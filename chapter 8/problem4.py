#write a recursive function to calculate the sum of first n natural numbers

# def sum(n):
#         if(n==1):
#                 return 1
#         return sum(n-1) + n

# n=int(input("Enter your number: "))
# print(f"{sum(n)} is the sum")

# #using the same logic used in factorial


def sum(n):
        if(n==1):
                return 1
        return sum(n-1)+n

n=int(input("Enter your number: "))
print(f"{sum(n)} is the sum of your natural numbers")