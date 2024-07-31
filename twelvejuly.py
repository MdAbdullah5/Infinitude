# import json
# def read(file_path):
#     with open(file_path,'r') as file:
#         data=json.load(file)
#         return data
# f=read("myjson.json")
# print(f)
# for a in f:
#     print(a)
#     print(f.get(a))
# try:
#     result="Hello"
#     print(int(result))
# except Exception as e:
#     print(e)
# try:
#     print(x)
# except Exception as e:
#     print(f"Error:{e}")

# try:
#     with open("MyData.txt",'r') as file:
#         data=file.read()
#         print(data)
# except FileNotFoundError:
#     print("No such file found")
# else:
#     print("Final Error")

# try:
#     # Code that may raise an exception
#     result = 10 / 1  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     # Handle the specific exception
#     print("Division by zero is not allowed")
# except Exception as e:
#     # Handle any other exceptions
#     print(f"An error occurred: {e}")
# else:
#     # Execute if no exception was raised
#     print("Division successful")
# finally:
#     # Always execute, used for cleanup actions
#     print("Cleanup")

