import json
#
data = {"name" : "anitha"}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
#
# json_string = json.dumps(data)
# print(type(json_string))
#
# # read a json variable inside a file and dump into a file or just assign to a string
#
# # Note that dump() takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.
# # Notice that the file-like object is absent since you aren’t actually writing to disk. Other than that, dumps() is just like dump().

# json_string = """
# {
#     "researcher": {
#         "name": "Ford Prefect",
#         "species": "Betelgeusian",
#         "relatives": [
#             {
#                 "name": "Zaphod Beeblebrox",
#                 "species": "Betelgeusian"
#             }
#         ]
#     }
# }
# """
# data = json.loads(json_string)
# print(data)
# print(type(data))
#
# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)
#     print(data)
#     print(type(data))
#
# # load funciton is with file and loads is with string object
#
# for key in data:
#     print(key)
#
# for value in data.values():
#     print(value)
#
# for key, values in data.items():
#     print(key, ":", values)
#     print(data['is_sw_only'])