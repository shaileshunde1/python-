#code to see if specific words are there in file and on line no

with open("log.txt") as f:
    lines = f.readlines()

word = "shailesh"
word2= "suyash"

lineno = 1 

for line in lines :
    if (word in line) or (word2 in line):
        print(f"Gubboys are mentioned in line : {lineno}")
        lineno += 1
        break
        

    else:
        print("gubboys are absent")
    




