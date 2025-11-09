#code to make star pattern

n=int(input("Enter the desired star pattern: "))

for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")

#note- if we had to make from - then we wouldve used 2*n+1
#print default goes to new line so end="" doesnt let that happen
