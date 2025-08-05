# request library in python provides simple way of make http request to interact with web services and API
#http methods- GET (used to retreive the data), POST, PUT, DELETE
#Headers- metadata about the request
#status codes- 200 (ok) 404 (not found), 500 (server error)

import requests
from requests.auth import HTTPBasicAuth
# response = requests.get("https://www.google10.com")
# print(response.status_code) #200 means success
# print(response.text) #to print response content

params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get("https://www.httpbin.org/get", params=params)
print(response.url) #show full URL with params

#post request with data
data = {"username": "admin", "password": "<PASSWORD>"}
response = requests.post("https://www.httpbin.org/post", data=data)
print(response.json()) #parse response as JSON

data = {'title': 'updated post'}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=data)
print(response.json())

#delete request
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)

#login using requests

username = ('abhijaypaliwal')
password = ('<PASSWORD>')
response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username, password))
print(response.json())
print(response.status_code)

#if you compare with API SERVERS, main work would be to expose the backed services by using restful or gRPC protocol to allow
# client to interact with data or services or ML models
# MCP model in contaxt is a orcherasted framework for managing ML models covering aspects like deployment versioning
# model train, rollback and governance

