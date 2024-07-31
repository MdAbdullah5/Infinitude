###########Operator Overloading for vectors
# class vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __str__(self): #Overloads the print()
#         return f"{self.i}i + {self.j}j + {self.k}k" #overloads the + operator
#     def __add__(self, other):
#         return vector(self.i+other.i, self.j+other.j , self.k+other.k)
#     def __sub__(self, other):
#         return vector(self.i-other.i,self.j-other.j,self.k-other.k)

#
# v1=vector(1,2,3)
# v2=vector(1,2,3)
# print(v1-v2)
# print(v1+v2)

############Property Decorators:Use to add attributes to a class"@Property is used as keyword"
# class Employee:
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
#     @property
#     def email(self):
#         s=f"{self.name}.{self.role}@gmail.com"
#         return s.lower()
#
#
# A=Employee("Raj","Dev")
# print(A.email)




##################MRO:Defines which function is called according to multiple inheritance
# class A:
#     def display(self):
#         print("A")
# class B():
#     def display(self):
#         print("B")
# class Demo(B,A):
#     def displa(self):
#         print("Demo")
# D=Demo()
# D.display()

###########Duck Typing:We dynamically pass the object and use its function.We pass object as an arguement.Something as Polymorphism
# class Cat:
#     def speak(self):
#         return "Meow!"
#
# class Dog:
#     def speak(self):
#         return "Woof!"
#
# class Duck:
#     def speak(self):
#         return "Quack!"
#
# def let_speak(animal):
#     print(animal.speak())
#
# # Create instances of different classes
# cat = Cat()
# dog = Dog()
# duck = Duck()
#
# let_speak(dog)

# class Specialstring:
#     def __len__(self):
#         return 21
#
#
# # Driver's code
# if __name__ == "__main__":
#     string = Specialstring()
#     print(len(string))
# print(len("jhf"))


######Shallow Copy:Refers to the original objects and when changes are made to the copy the original contents are also changed
import copy
# Original=[1,2,3,4]
# s=copy.copy(Original)
# s[0]=0
# print(s)
# print(Original)
# #
#
# #Deep Copy:Doesn't affect the original copy and newly memory is created
# Original=[1,2,3,4]
# r=copy.deepcopy(Original)
# r[0]=0
# print(r)
# print(Original)


# import copy
#
# # Original list containing a nested list
# original_list = [[1, 2, 3], [4, 5, 6]]
#
# # Shallow copy
# shallow_copy = copy.copy(original_list)
#
# # Modify the nested list in the shallow copy
# shallow_copy[0][0] = 100
#
# # Print both original and shallow copied lists
# print("Original List:", original_list)  # Output: Original List: [[100, 2, 3], [4, 5, 6]]
# print("Shallow Copy:", shallow_copy)


####Type Hintings:Giving Hints to the user to use appropriate data may not affect the code
# def greet(name: str) -> str:
#     return f"Hello, {name}"
#
# # Function call with correct type
# result = greet("Alice")
# print(result)  # Output: Hello, Alice
#
# # Function call with incorrect type (no error at runtime due to dynamic typing)
# result = greet(True)
# print(result)


####Annotations:special method to print the type of attributes of a function and their return type
# def calculate_area(length: float, width: float) -> str:
#     """Calculate the area of a rectangle."""
#     return length * width
#
# # Annotations with type information
# print(calculate_area.__annotations__)
# print(type(calculate_area(1.0,9)))



######Context Managers:Use to handle files networks dbs
# class File:
#     def __init__(self,file,mode):
#         self.file=file
#         self.mode=mode
#     def __enter__(self):
#         print(f"Opening {self.file}...")
#         f=open(self.file,self.mode)
#         return f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"Closing {self.file}....")
# with File("MyData.txt",'r') as f:
#     print("File Operations")
#     k=f.read()
#     print(k)