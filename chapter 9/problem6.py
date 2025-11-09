#code to see if specific words are there in file

with open("log.txt") as f:
    content = f.read()

word = "python"
word2= "valorant"
if (word in content):
    print("koi chakka python seekh raha hai")

if(word2 in content):
    print("koi bhadwa valo khel raha hai")
