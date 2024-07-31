# dict={1:'a',2:'b',3:'c',4:'d',5:'e'}
# print("Assignment-1")
# for keys in dict:
#     print(keys)
# print('\n')
# for keys in dict:
#     print(dict.get(keys))
#
# dict.popitem()
# print(dict)
#
# dict.setdefault("car","tesla")
# print(dict)
#
# list_of_lists = [[key, value] for key, value in dict.items()]
# print(list_of_lists)
#
# k=[]
# for keys in dict:
#     k.append(keys)
#     k.append(dict.get(keys))
#
# print(k)
#
# print("\n")
# print("Assignment-2")
# print(k[:8])
# print(k[8])
#
# a=[1,4,5,4,6,3,5]
# a.sort()
# print(a)
# a.reverse()
# print(a)
#
# intlist=[i for i in k if isinstance(i,int)]
# intlist.sort()
# print(intlist)
#
# strlist=[i for i in k if isinstance(i,str)]
# strlist.sort()
# print(strlist)
#
# print("\n")
# print("Assignment-3")
# for i in range (101):
#     if(i%5==0):
#         print(i)
#
# n=0
# print("\n")
# print("while")
# while(n<=5):
#     print(n)
#     n+=1
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)