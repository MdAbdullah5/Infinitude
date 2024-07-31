# class Employee():
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
#     def emp2(self):
#         print("Employee name is :",self.name,"Role is:",self.role)
# class Developer(Employee):
#     def __init__(self,salary,name,role):
#         super().__init__(name,role)
#         self.salary=salary
#     def emp2(self):
#         print("Employee name is :",self.name,"role is: ",self.role,"Salary is: ",self.salary)
# # emp1=Developer("Aditya","Dev")
# # emp1.emp()
# # subclass=Developer("Anish","Tester")
# # subclass.emp2()
# Emp=Developer(10000,"Anish","Dev")
# Emp.emp2()
# mod =Employee("Mani","Tester")
# mod.emp2()


# class Overload:
#     def product(a, b):
#         p = a * b
#         print(p)
#     def product(a,b,c):
#         p=a*b*c
#         print(p)

# class FileOps:
#     def __init__(self,file,data,dest):
#         self.file=file
#         self.data=data
#         self.dest=dest
#     def read(self):
#         with open(self.file,'r') as f:
#             k=f.read()
#             print(k)
#     def write(self):
#         with open(self.file,'a') as f:
#             f.write(self.data)
#     def copy(self):
#         with open(self.file,'r') as f:
#             with open(self.dest,'a') as k:
#                 r=f.read()
#                 for g in r:
#                     k.write(g)
#
#
# G=FileOps("copy.txt","hi","hi.txt")
# G.read()
# G.write()
# G.copy()

class MathOperations:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a/b
# res=MathOperations.divide(1,2)
# print(res)

import json
import yaml

class ConfigParser:
    @staticmethod
    def parsejson(file):
        with open(file,'r') as f:
            config=json.load(f)

        return config
    @staticmethod
    def parseyaml(file):
        with open(file,'r') as f:
            c=yaml.safe_load(f)
        return c
# k=ConfigParser.parseyaml("sample.yaml")
# print(k)

class Perimeter:
    pi=22/7
    @staticmethod
    def rectangle(l,b):
        return 2*(l+b)

    @staticmethod
    def square(a):
        return 4*a

    @staticmethod
    def circle(r):
       return 2*Perimeter.pi*r


# print(Perimeter.circle(4))
import requests
class Api:
    @staticmethod
    def get(url):
        r=requests.get(url)
        return r.content
    @staticmethod
    def post(url,data):
        r=requests.post(url,data)
        return r.content
# d={
#     "name": "morpheus",
#     "job": "zion resident"
# }
# print(Api.post("https://reqres.in/api/users?page=2",d))
# print(Perimeter.circle(0.5))