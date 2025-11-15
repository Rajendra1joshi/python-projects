#updating the json file through python

import json 

with open('first_json.json','r') as file:
    data = json.load(file)

data['Marks'] = 90

with open('first_json.json','w') as file:
    json.dump(data,file,indent=4)