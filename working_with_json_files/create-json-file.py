import json

my_dict = {'Name' : 'Narendra' , 'skills' : ['Python' , 'shell' , 'yaml' , 'AWS']}

req_file = "myinfo.json"

fo = open(req_file , 'w')
json.dump(my_dict , fo , indent = 4)

fo.close()