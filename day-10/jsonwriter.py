import json
data = {
    "name":"jack",
    "age": 19
} 
with open("jsondata.json", "w") as file:
    json.dump(data, file,indent=4)