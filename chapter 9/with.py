f = open("myfile.txt")
print(f.read())
f.close()


#also can be written as 
with open("myfile.txt") as f:
    print(f.read())

#by this method you dont have to close this file  