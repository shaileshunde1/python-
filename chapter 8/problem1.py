#a program using fucntions to write the greatest of 3 numbers

def grt(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    

a=int(input("Enter your number here : "))
b=int(input("Enter your number here : "))
c=int(input("Enter your number here : "))

greatest=grt(a,b,c)
print(f"{greatest} is the greatest of all numbers")



#also can be done as

a=int(input("Enter your number here : "))
b=int(input("Enter your number here : "))
c=int(input("Enter your number here : "))

print(f"{max(a,b,c)} is the greatest of all numbers")