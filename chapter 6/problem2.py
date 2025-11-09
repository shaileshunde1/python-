#basic program to take marks of 3 subjects and state pass or fail

marks1=int(input("Enter your marks for subject1 here : "))
marks2=int(input("Enter your marks for subject2 here : "))
marks3=int(input("Enter your marks for subject3 here : "))

total_percentage =(100)*((marks1+marks2+marks3)/300)
if(total_percentage>=40 and marks1>=32 and marks2>=32 and marks3>=32):
    print("You are pass",total_percentage)
    
else:
    print("You are fail",total_percentage)