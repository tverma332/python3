import json

req_file = "myjson.json"

fo = open(req_file , 'r')
print(json.load(fo))

fo.close()