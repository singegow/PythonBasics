# key value pair
# Name : Anitha
# phone : 123
# email : anitha.com
# customer = {
#     "name" : "anitha",
#     "phone" : "123",
#     "email" : "anitha.com"
# }
# print(customer)
# print(customer["name"])
#print(customer["Name"])
#   File "C:/python/PythonPrograms/From_Mosh/dictionaries.py", line 12, in <module>
#     print(customer["Name"])
# KeyError: 'Name'

# In the above if we pass anything which doesnt exists the code will fail.
# Rather than that we can use "get" method to retrieve it. Here it doesnt fail, it just says "none" if the value doesnt exists
# print(customer.get("name"))
# print(customer.get("Name"))
# # get can also be used to assign a value to the key if the key pair doesnt exists
# print(customer.get("Name", "NEW_ANITHA"))
# print(customer)
# # Adding new key value to pair to dicitionary
# customer["birthdate"] = "jan 1"
# print(customer)
# customer["birthdate"] = "Mau 12"
# print(customer)
# Exercise
user_input = input("please enter your phone number:")
phone_num = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

#empty string
output_str = ""
for number in user_input:
    converted = phone_num.get(number,"!")
    output_str += converted + " "
print(output_str)