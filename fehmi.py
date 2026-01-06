import requests

url="https://jsonplaceholder.typicode.com/posts/1"





result=requests.delete(url)

print("status code:",result.status_code)

