def add(a,b):
    return a+b
def sub(a,b):
    return abs(a-b)
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def cal(op,o1,o2):
    if(op=='+'):
        return o1+o2
    elif(op=='-'):
        return abs(o1-o2)
# if __name__ == "__main__":
#     add(1,2)
#print("out")
def main():
     print("FIrst module name:{}".format(__name__))

if __name__ == "__main__":
    main()