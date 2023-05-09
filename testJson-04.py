# imports the JSON library to work in python
import json

# assign the JSON data to a variable
json_data = """{
                "data": [
                    {
                        "type": "articles",
                        "id": "1",
                        "attributes": {
                            "title": "Working with JSON Data in python",
                            "description": "This article explains the various ways to work with JSON data in python.",
                            "created": "2020-12-28T14:56:29.000Z",
                            "updated": "2020-12-28T14:56:28.000Z"
                        },
                        "author": {
                            "id": "1",
                            "name": "Aveek Das"
                        }
                    }
                ]
            }"""

# Print the datatype of the original variable before deserialization
print(f'Datatype before deserialization: {str(type(json_data))}')
print("\n")

# Deserialize the JSON to a python dictionary object
new_data = json.loads(json_data)

# Print the datatype of the new variable after deserialization
print(f'Datatype after deserialization: {str(type(new_data))}')
print(new_data)
print("\n")


# Serialize the python dictionary object back to JSON string
reset_data = json.dumps(new_data)

# Print the datatype of the new variable after deserialization
print(f'Datatype after serialization: {str(type(reset_data))}')
print(reset_data)
