#program to filter a list of numbers which are divisible by 5

list2 = [10,23,45,60,33,22,15,90,88,120,55]

def div_by_5(n):
    if n%5==0:
        return True
    return False
divlist = filter(div_by_5, list2)
print(f"numbers divisible by 5 are {list(divlist)}")