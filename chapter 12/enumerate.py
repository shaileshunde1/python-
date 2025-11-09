l = [12,55,67,78,89]
 
index = 0 
for item in l:
    index+= 1
    print(f"number at {index} is {item}")

#the same thing can be optimised by enumerate

for index, item in enumerate(l):
    print(f"number at {index} is {item}")
