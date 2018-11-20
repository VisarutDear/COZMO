import json

# some JSON:
x = '{ "name":"DEAR", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y["name"])

