file="C:\\Users\\abdul\\PycharmProjects\\pythonProject2\\MyData.txt"
t=input("enter contents")
f=open(file,'a')
k=open("copy.txt",'a')


f.write(t)
i=open("MyData.txt",'r')
c=i.readline()
for line in c:
    k.write(line)
j=open("copy.txt",'r')