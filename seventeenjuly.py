# class Employee():
#     def __init__(self):
#
#         pass
#     def add(self,x,y):
#         print(x+y)
#
# e=Employee()
# print(e.add(1,2))

#Encapsulation
class Person():
    def __init__(self):
        self.__name="A"
        self._age=2
    def _p(self):
        print(self.__name)

A=Person()
A._p()

