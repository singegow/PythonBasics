first = 'Jhon'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
# The above approach is clumsy and harder to visualise the output when the strings becomes ongs
# f is used to represent that its a formatted string
msg = f'{first} [{last}] is a coder'
# {} defines the placeholder in the formatted string
print(message)
print(msg)