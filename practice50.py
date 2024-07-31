import math


def multi(i,j):
    l=[]
    for k in range(i,j+1):
        if(k%7==0) and (k%5!=0):
            l.append(k)
    print(l)
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
def squares(n):
    d=dict()
    for i in range(0,n+1):
        d[i]=i*i
    print(d)
# multi(2000,2500)
# print(fact(3))
# squares(7)
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input()
#
#     def printString(self):
#         print(self.s.upper())
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
# s=str(input("Enter numbers use seprator as ',':"))
# l=s.split(",")
# i=[int(math.sqrt((2*int(x)*50/30))) for x in l ]
# print(i)

#2d Array
# s=input("Enter Dimensions")
# d=[int(x) for x in s.split(" ")]
# print(d)
# row,col=d
# matrix=[[0 for i in range(col)] for j in range(row)]
#
# for i in range(row):
#     for j in range(col):
#         matrix[i][j]=i*j
# print(matrix)

# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
#
# for sentence in lines:
#     print(sentence)

# Odd List comprehension
# s=input("Enter Numbers:")
# l=[int(x) for x in s.split(",") if (int(x)%2!=0)]
# print(l)

# net=0
# while True:
#     s=input()
#     if not s:
#         break
#
#     values=s.split()
#     op=values[0]
#     a=int(values[1])
#     if op=='D':
#         net+=a
#     if op=='W':
#         if net-a<0:
#             print("Low Balance")
#             break
#         net-=a
# print(net)
def reverse(s):
    return s[::-1]
s="hi"
print(reverse(s))