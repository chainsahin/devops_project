import requests
import json
import sys

response=requests.get("https://www.google.com/?hl=tr")

if response.status_code==200:
    print("API sorgulaması başarılı durum kodu:",response.status_code)
else :
     response.status_code==404
     sys.exit(1)
     print("API sorgulaması başarısız durum kodu:",response.status_code)




