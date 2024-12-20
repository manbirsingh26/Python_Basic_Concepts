"""
Convert a Python object containing all the legal data types:
"""
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "Ford Mustang Gt 500", "engine": "V8"},
    {"model": "Lamborghini Urus SE", "engine": "V6 Hybrid"}
  ]
}
y = json.dumps(x)
print(y)

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result
# Use the indent parameter to define the numbers of indents:
y = json.dumps(x, indent=4)
print(y)

# You can also define the separators, default value is (", ", ": "),
# which means using a comma and a space to separate each object,
# and a colon and a space to separate keys from values:
# Example
# Use the separators parameter to change the default separator:
y = json.dumps(x, indent=4, separators=(". ", "="))
print(y)

# We can also order the result in json
# Example using sort_keys
y = json.dumps(x, sort_keys=True, indent=4)
print(y)

