# def pattern(n):
#     for i in range(n,0,-1):
#         print("*"*i)
        

# n=int(input("Enter your star value: "))
# pattern(n)

def pattern(n):
    if(n==0):
        return 0
    print("*" *n)
    pattern(n-1)


n=int(input("Enter your star value: "))
pattern(n)

#here we have used recursion