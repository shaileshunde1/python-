import random

n = random.randint(1,20)
guesses = 1
a= -1


while(a != n):
    
    a = int(input("Enter your guess : ")) 
    if(a<n):
        print("Higher number please")
        guesses += 1

    elif(a>n):
        print("Lower number please")
        guesses += 1

print(f"youve guessesed the correct number {n} in {guesses} guesses")