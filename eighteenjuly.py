# class Base:
#     def __init__(self):
#         self._a=1
#     def _p(self):
#         print("protected")
# class Derived(Base):
#     def __init__(self):
#         Base().__init__(self)
#         self._a=2

# Abstract class and Method
from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def test1(self):
        pass
    @abstractmethod
    def test2(self):
        pass
class Person2(Person):
    def test1(self):
        print("Overriden Abstract Method using Inheritance")
    # def test2(self):
    #     pass
class Person3(Person2):
    def test2(self):
        print("Again Overriden")
obj=Person3()
obj.test2()
# class emp:
#     def emp(self):
#         print("emp")
# class dev(emp):
#     def de(self):
#         print("dev")
