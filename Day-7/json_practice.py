import json

details = {
    "Name":"Raj",
    "Country":"Nepal",
    "Marks":"83"
}

with open('first_json.json',"w") as file:
    json.dump(details,file,indent=4)

# indent means space , it makes the json file nice, easy to understand