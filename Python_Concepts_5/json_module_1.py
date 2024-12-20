# importing the json_module
import json

# Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# Result will be a Python Dictionary
x = '{"Name": "Manbir", "Age": 22, "City": "Jammu"}'  #some json
#print(type(x))
y = json.loads(x)
#print(type(y))
print(y)

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
x1 = {
    "Name": "Manbir",
    "Age": 22,
    "City": "Jammu",
    "Profession": "Python Developer"
}
y1 = json.dumps(x1)
print(y1)  #This is a JSON string



