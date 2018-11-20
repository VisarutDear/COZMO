import json

# some JSON:
x = '{ "name":"DEAR", "age":18, "city":"Bangkok", "medname":"TYLENOL","amount":"1","time":"12:00"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("NAME :",y["name"])
print("MEDNAME :",y["medname"])
print("AMOUNT :",y["amount"])
print("TIME :",y["time"])
