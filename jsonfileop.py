import json
def write_json(data,file="myjson2.json"):
    with open(file,'w') as f:
        json.dump(data,f,indent=4)
file=open("myjson.json",'r')
x=file.read()
t=json.loads(x)
# print(f)
# f=open("myjson2.json",'w')
write_json(data=t,file="myjson2.json")


