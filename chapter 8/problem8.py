# def table(n,i=1):
#     if i>10 :
#         return
#     print(f"{n} x {i} = {n*i}")
#     table(n, i+1)



# n=int(input("Enter your number : "))
# table(n)


def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n=int(input("Enter your number: "))
multiply(n)