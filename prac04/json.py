#1
json_text = '{"name": "Aman", "age": 20, "is_student": true}'
#2
import json
json_text = '{"name": "Aman", "age": 20}'
data = json.loads(json_text)
print(data["name"])
print(data["age"])
#3
import json
person = {
    "name": "Aman",
    "age": 20,
    "student": True
}
json_string = json.dumps(person)
print(json_string)
#4
import json
data = {
    "city": "Almaty",
    "population": 2000000
}
with open("data.json", "w") as file:
    json.dump(data, file)
#5
import json
with open("data.json", "r") as file:
    data = json.load(file)
print(data)
#6
import json
with open("sample-data.json", "r") as file:
    data = json.load(file)
for item in data:
    print(item)