def first(fistname , lastname):
    print("Firstname" + "  "+ fistname+" " +" lastname   "+lastname)
first("joy","roy")

def myfun(cars):
    for c in cars:
        print(c)

cars=["hello","hi","gm"]
myfun(cars)


def multiargs(*args):
    print(args)
multiargs(1,2,3,4)

#Keyword arguements
def keywrd(**key):
    print(key["test2"])
keywrd(test1=1,test2=2,test3=3)

# Lambda Functions
x= lambda a,b : a+b
print(x(5,7))

#Return Function
def multi(t):
    return t*5

print(multi(4))

