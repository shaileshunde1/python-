# cm = inch x 2.54
# inch = (cm/2.54)

def conversion(n):
    a= (n*2.54)
    print(f"Conversion is :{a} cm")
    if(a<15):
        print("Kaafi chhota hai yaar")
        return a

n=int(input("Enter kitne inch ka hai : "))
conversion(n)

#khud se code kiya hai