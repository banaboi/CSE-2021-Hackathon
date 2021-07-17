import requests

BASE_URL = "http://127.0.0.1:5000/"

data1 = {
    "email" : "hell this is my email",
    "password" : "this is my password"
}

data2 = { 
    "fname" : "Luke",
    "lname" : "Tomic", 
    "phone" : 405331678,
    "email" : "bigluke@hotmail.com",
    "password" : "password", 
    "edu_category" : "Science",
    "teach_level" : "High School",
    "contacts" : "discord and slack"
}

output = requests.post(f"{BASE_URL}/signin", data=data1)
print(output)
output = requests.post(f"{BASE_URL}/stu_sign_up")
print(output)
