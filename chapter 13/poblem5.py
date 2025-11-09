#write a program to find the max of no in a list using reduce function
from functools import reduce

l= [3,5,7,22,8,6,4,10,12,15]

def max_num(a,b):
    if a>b:
        return a
    return b

maxx = reduce(max_num, l)
print(f"the maximum number in the list is {maxx}")
