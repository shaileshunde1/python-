#we can also raise errors by our onw

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if (b==0):
    raise ZeroDivisionError("mat kar lala")

else:
    print(f"The diviion of a/b is {a/b}")

#pretty accurate code for first try