import json
x =  '{ "name":"Tupac", "age":25, "city":"Las Vegas"}'
y = json.loads(x)
print(y["age"]) 

import json
print(json.dumps({"name": "Christopher", "age": 24}))
print(json.dumps(["BMW", "Mercedes"]))
print(json.dumps(("BMW", "Mercedes")))
print(json.dumps("Howdy"))
print(json.dumps(52))
print(json.dumps(13.37))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 

import json

x = {
  "name": "Kanye",
  "age": 47,
  "married": False,
  "divorced": True,
  "children": ("North","Saint","Psalm","Chicago"),
  "pets": True,
  "cars": [
    {"model": "Lamborghini Aventador LP 700-4", "mpg": 9},
    {"model": "Rolls-Royce Phantom VIII", "mpg": 12}
  ]
}
print(json.dumps(x))


json.dumps(y, indent=4)



json.dumps(x, indent=4, separators=(". ", " = "))