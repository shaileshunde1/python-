#to make list based on existing list

mylist = [1,3,4,5,6,7,8]

squaredlist = []
for item in mylist:
    squaredlist.append(item*item)

print(squaredlist)

#pretty decent approach

betterlist = [item*item for item in mylist]

print(betterlist)

#comprehensive list

l =[1, 5 , 10]

complist = [i*i for i in l]

print(complist)