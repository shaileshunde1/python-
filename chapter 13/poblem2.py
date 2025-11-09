#function to take input of name,marks and phone no and format it

n=input("enter your name:")
p=input("enter your phone number:")
m=input("enter your marks:")


a = "{} has scored {} marks and his/her phone no is {}" .format(n,m,p)
print(a)