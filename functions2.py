# def myfunc(x):
#     return  5*x;
#
# print(myfunc(5))
#
# a=lambda x,y:x+y
# print(a(9,9))
#
# def test(text):
#     return text.upper()
# def test2(func):
#     print("this is starting")
#     v=func("this is inside")
#     print(v)
#
# test2(test)

# def fact(n):
#     if(n==0):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(4))

# def add(*num):
#     t=0
#     for n in num:
#         t+=n
#     return t
# print(add(1,2,3))

# import paramiko
# def ssh_connect(host,username,password,port):
#     try:
#         client=paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(hostname=host,username=username,password=password,port=port)
#         print("Connection is Successful")
#     except Exception as e:
#         print(f"Error:{e}")
#
#
#
# ssh_connect()

