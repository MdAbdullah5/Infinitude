#######MAgic methods are used to manipulate the objects
# class Person:
#     def __init__(self,msg):
#         self.msg=msg
############has only for current users
#     def __repr__(self):
#         return "Person({})".format(self.msg)
######has more priority used for everyone
#     def __str__(self):
#         return f"{self.msg}"
# e=Person("Hello")
# print(e)

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f"({self.x},{self.y})"
#     def __repr__(self):
#         return f"Point({self.x},{self.y})"
# p=Point(1,2)
# print(p)

#########__len__
# class Person:
#     def __init__(self,msg):
#         self.msg=msg
#     def __len__(self):
#         return len(self.msg)
# e=Person("Hello")
# print(len(e))
#######set and get
# class Dict:
#     def __init__(self,dict):
#         self.dict=dict
#     def __getitem__(self, item):
#         return f"{item}:{self.dict[item]}"
#     def __setitem__(self, key, value):
#         self.dict[key]=value
# e=Dict({1:'a',2:'b'})
# e[3]='c'
# print(e[3])
# import sys
# l=[1,2,3]
# y=iter(l)
# print(next(y))
# print(sys.getsizeof(y))
# print(next(y))
# print(sys.getsizeof(y))
# for i in l:
#     print(sys.getsizeof(i))
#     print(i)
####Square of numbers using for loop and iter
import sys
class square:
    def __init__(self,max):
        self.max = max

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current <= self.max:
            result = self.current**2
            self.current += 1
            return result
        else :
            raise StopIteration

x = square(5)
y = iter(x)
z = next(y)
print(z)
print(sys.getsizeof(z))

