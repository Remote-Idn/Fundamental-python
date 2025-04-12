'''
Belajar Membuat Dictionary dan Menggunakan Format JSON
'''

users = [{
    "ID" : 1,
    "Name" : "Dave",
    "Age" : "18",
    "Email" : "Dave@xyz.com"
    },
{
    "ID" : 2,
    "Name" : "Ruth",
    "Age" : "21",
    "Email" : "Ruth@xyz.com"
}
]
print(users)

import json
result = json.dumps(users)
print(result)
print(type(result))

with open("result.json", "w") as file:
    json.dump(users, file)