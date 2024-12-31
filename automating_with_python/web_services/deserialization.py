import json

people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {"office": "802-867-5309", "cell": "802-867-5310"},
        "department": "IT Infrastructure",
        "role": "Systems Administrator",
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {"office": "684-348-1127"},
        "department": "IT Infrastructure",
        "role": "IT Specialist",
    },
]

with open("people.json", "r") as json_string:
    people = json.load(json_string)

print(type(people))


json_string = json.dumps(people)
print(json_string)
print(type(json_string))

people = json.loads(json_string)
print(people)
print(type(people))
