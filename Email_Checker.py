import json
from urllib.request import urlopen

'''
Simple Email Checker
'''

email = input("Email : ")

key = "IhuPynxZSqjfvX8T0e2cFkAa65gYVGMK"

url = "https://emailverifierapi.com/v2/?apiKey=" + key + "&email=" + email

response = urlopen(url)
data = json.load(response)
details=data['details']

if details == "The mailbox exists.":
    print("True Email!")
else:
    print("Fake Email!")
