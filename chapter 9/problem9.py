#code to see if 2 files have same content

with open ("this.txt") as f:
    content = f.read()
    
with open ("thiscopy.txt") as f:
    content2 = f.read()

if content == content2 :
    print("The insides are identical")

else:
    print("Insides are not identical")
    