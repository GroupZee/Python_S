import json
trac={"name":"kelly",
      "age":10,
      "City":"Kampala"
}
file_path='sthNew.json'
with open(file_path, 'w') as file:
    json.dump(trac,file)