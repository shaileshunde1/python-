#reduce example

from functools import reduce

l = [1,20,30,2,40,50]

def multiply(a,b):
    return a*b
product = reduce(multiply, l)
print(product)