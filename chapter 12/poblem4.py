#program to display a/b where a and b are integers, if b=0 display infinite by 
#handling the zerodivisionerror 

a = int(input("First number daalde chotu : "))
b = int(input("Second number daalde chotu : "))

if(b==0):
    raise ZeroDivisionError("mat kar lala")

else:
    print(f"The division of a/b is {a/b}")


#there is also another way to solve this 

try:
    c = int(input("Third number daalde chotu : "))
    d = int(input("Fourth number daalde chotu : "))
    print(a/b)

except ZeroDivisionError as v:
    print("sudhar lavdya")

