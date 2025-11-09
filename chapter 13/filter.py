#filter example

l =[1,2,3,4,5,6,7,8,9,10]

def even_check(n):
    if n%2==0:
        return True   
    return False

evenlist = filter(even_check, l)
print(list(evenlist))