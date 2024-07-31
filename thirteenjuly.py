import string


def wordcount(file):
    word_freq={}
    with open(file,'r') as f:
        contents=f.read()
        words=contents.split()

        for word in words:
            if word in word_freq:
                word_freq[word] +=1
            else:
                word_freq[word]=1

    for word,freq in word_freq.items():
        print(word,freq)
wordcount("copy.txt")

def reversestring(s):
    return s[::-1]
print(reversestring("Hello"))
def stringlength(s):
    c=0
    for a in s:
        c+=1
    return c
print(stringlength("hello"))

s="hello"
p=""
for i  in range(len(s)-1,-1,-1):
    p+=s[i]
print(p)
def fib(n):
    fib=[]
    if(n>=1):
        fib.append(0)
    if(n>=2):
        fib.append(1)
    for i in range (2,n):
        next =fib[-1] + fib[-2]
        fib.append(next)
    return fib
print(fib(5))
def readLines(file):
    with open(file,'r') as f:
        l=0
        for lines in f:
            l+=1

    return l
print(readLines("copy.txt"))

p="Hello my name is john"
currentword=[]
words=[]
for a in p:
    if(a!=' ' and a!='\t' and a!='\n'):
        currentword.append(a)
    else:
        if currentword:
            words.append(''.join(currentword))
            currentword=[]
if currentword:
    words.append(''.join(currentword))
print(words)


def flatten_list(nested_list):
    flattened_list = []

    def flatten_helper(nested):
        for item in nested:
            if isinstance(item, list):
                flatten_helper(item)
            else:
                flattened_list.append(item)

    flatten_helper(nested_list)
    return flattened_list
print(flatten_list([1, [2, 3, [4, 5], 6], [7, 8], 9]))


def reversefile(file):
    with open(file,'r') as f:
        list=f.readlines()
        list.reverse()
        for lines in list:
            print(lines)

reversefile("copy.txt")

s="This is , a car?"
p=''.join([char for char in s if char not in string.punctuation ])
print(p)
l=[1,3,5,7,9]
p=[2,4,6,8]
i=0
j=0
k=[]
while i<len(l) and j<len(p):
    if(l[i]<p[j]):
        k.append(l[i])
        i+=1
    else:
        k.append(p[j])
        j+=1
while i<len(l):
    k.append(l[i])
    i+=1
while j<len(p):
    k.append(p[j])
    j+=1
print(k)