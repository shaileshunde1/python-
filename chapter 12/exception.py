#program to avoid code crashing

try:
    a  = int(input("Enter your number :  "))
    print(a)

except Exception as e:
    print(e)

#we can also give other errors

except ValueError as v:
    print(v)

print("Agli baar se dhyaan rakhna")