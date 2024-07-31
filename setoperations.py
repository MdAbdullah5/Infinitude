a={1,2,"apple",'z'}
y={"apple","banana"}
print(a)
a.add(3)
print(a)
z=a.difference(y)
print(z)
# a.difference_update(y)
print(a)
a.discard('z')
r=a.intersection(y)
print(r)
p=a.union(y)
print(p)
