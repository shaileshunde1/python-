#code to use lambda
#basically you can assign variables to lambda
#where as in you can make lambda a function

square =  lambda x :  x*x
print(square(55))

sum =  lambda a,b,c: a+b+c
print(sum(1,2,3))


#also can be done by traditional method
def square(n):
    return n*n

print(f"the square of is {square(55)}")
