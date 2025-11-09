# formula is c/5=(f-32)/9
# can also be written as c=5*(f-32)/9



# def f_to_c(f):
#     return 5*(f-32)/9

# f=int(input("Enter temperature in Fahrenheit : "))

# c= f_to_c(f)
# print(f"Conversion is {round(c,2)} °C")



# okay so lets write the whole code again without chat

def fun(f): 
    return 5* (f-32)/9


f=int(input("Enter temp in F here : "))
c=fun(f)
print(f"Conversion is {round(c,2)} degree celsius")
