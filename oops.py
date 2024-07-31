class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def  test(self):
        print(self.name,self.age)


class B():
    def test1(self):
        print("Welcome to classes")




person1 = Person("Alice",22)
person1.test()
print(person1.name)
print(person1)
p=B()
p.test1()