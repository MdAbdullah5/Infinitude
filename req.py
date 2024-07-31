import requests
r=requests.get("https://reqres.in/api/users?page=2")
print(r.content)
data={
     "id":"90",
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"

}
res=requests.post("https://reqres.in/api/login",data)
print(res.content)
print(res.status_code)
d={
    "name": "morpheus",
    "job": "zion resident"
}
res1=requests.put("https://reqres.in/api/users/2",d)
print(res1.content)
