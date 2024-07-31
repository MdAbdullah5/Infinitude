def Hi(fname,lname):
    print("Welcome:",fname +" "+lname)
Hi("Abdullah","Habeeb")

x=lambda n:n**3
print(x(7))

def Names(*args):
    print(args[1])
Names("Abdullah","Rahman")

def fruits(**f):
    print(f["fruit2"])
fruits(fruit1='mango',fruit2='banana')