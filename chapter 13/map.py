#basically we can map idk what to what but yea

l = [1,2,3,4,5,6,7,8,9]

square = lambda x: x*x

sqlist = (map(square, l))

print(list(sqlist))

#we gonna code again without seeing above

l2 =[11,12,13,14]

cube = lambda x: x*x*x

cubelist = map(cube,l2)
print(list(cubelist))