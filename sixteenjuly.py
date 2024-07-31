# #Multi Level Inheritance
# class Employee:
#     def __init__(self):
#         pass
#     def test1(self):
#         print("Super Class")
#
# class Developer(Employee):
#     # def __init__(self):
#     #     super().__init__()
#     def test2(self):
#         print("sub class")
# class Tester(Developer):
#     def test3(self):
#         print("Tester Class")
# e=Tester()
# e.test1()
# e.test2()
# e.test3()

##Multiple Inheritance
# class Add():
#     def sum(self,a,b):
#         return a+b
# class Multiply():
#     def multiplication(self,a,b):
#         return a*b
# class Derived(Add,Multiply):
#     def divide(self,a,b):
#         return a/b
# p=Derived()
#
# print(p.sum(1,2))
# print(issubclass(Derived,Multiply))
# print(isinstance(p,Multiply))
#Kinds of variables : class,instance(constructor variables),static,local
# class Employee:
#     #Static Variable
#     company="Infinitude"
#     def __init__(self):
#         #Local Variable
#         self.name="Anas"
#         self.role="Tester"
# e=Employee()
# print(e.company)

