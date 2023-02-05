# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

# Akz = Abdul khalek zouhori

import json

# sample json
UserJSON_Akz = '{"first_name": "json" , "last_name": "brad" , "age": 35}'

# parse to dict
user = json.loads(UserJSON_Akz)

print(user)
print(user['first_name'])



car_Akz = {'make': 'ford' , 'model': 'croen v', 'year': 2001}

carJSON = json.dumps(car_Akz)
print(carJSON)

