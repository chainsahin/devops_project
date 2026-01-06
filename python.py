import json


# with open("files/data.json","r",encoding="utf-8") as f:
#     result=json.load(f)

#     print(type(result))

#     print(f"Name:{result['name']}")
#     print(f"Age:{result['age']}")
#     print(f"City:{result['city']}")
#     print("Hobbies",end=" ")

#     for item in result["hobbies"]:
#         print(item,end=" ")


person={"name":"Fehmi","age":20,"city":"giresun","hobbies":
        ["kodlama","futbol","basketbol"]}
result=json.dump(person)

print(type(result))
print(result)