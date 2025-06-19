import json
file_path = 'sthNew.json'
with open(file_path,'r')as file:
    a = json.load(file)
#display the contents of the json file
print(a)