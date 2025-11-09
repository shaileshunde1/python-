#used to code efficiently from py 3.8

#old code
n =[1,23,34,4]
b = len(n) 

if(b>5):
    print("Big ah list")

else:
    print("chalta hai")


#new code
if(n := len([1,2,3,4])) >5 :
    print("Big ah list")
else:
    print("Gubboy")


#idk i took a break
if (n:= len([1,2,3,4,] >5)):
    print("ggwp")


if (n:= len([1,2,3,4,5]))  >5:
    print("ok hai darling")