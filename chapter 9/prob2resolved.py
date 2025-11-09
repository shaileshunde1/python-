import random

def game():
    print("Youre playing the game sir")
    score = random.randint(1,100)
    print(f"Your score is {score}")

    with open("hiscore.txt") as f:
        hiscore=f.read()
        if (hiscore!= ""):
            hiscore=int(hiscore)
        else:
            hiscore = 0
    
    with open("hiscore.txt", "w") as f:
        if(score > hiscore):
            f.write(str(score))

    return score
    
game()

#did it almost by myself and i do understanding the basics of code ,
# just a few syntax errors