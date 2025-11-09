#c9ode to copy 1 file's content to another

with open("this.txt") as f:
    content=f.read()

with open("thiscopy.txt", "w") as f:
    f.write(content)