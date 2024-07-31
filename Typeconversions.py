l=[1,2,3,4]
k=tuple(l)
print(k)
print(k.index(1))
p=list(k)
print(p)
s=set(l)
print(s)
h=str(l)
print(h)

string = "This is a test string"
dict = dict((word, "") for word in string.split())
print(dict)

# for keys in dict:
#     dict.update(keys,string.count(keys))