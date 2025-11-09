n = int(input("Enter your number : "))

list =[]

list.append(n)

squaredlist =[n*n for i in list ]

print(f"the square is {squaredlist[0]}")