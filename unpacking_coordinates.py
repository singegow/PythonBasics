coordinates = (1,2,3)
# If we need to mutltiply all coordinates, then we need to use this code
multiply = coordinates[0] * coordinates[1] * coordinates[2]
print(multiply)
# One more easier approach would be to assign these to a varialbe and use when necessary
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
multiply = x * y * z
print(multiply)
# all of the above can be reduced using unpacking feature in python
x, y, z = coordinates
multiply = x * y * z
print(multiply)
# This feature can be used in list as well
list = [1,2,3]
x,y,z = list
multiply = x * y * z
print(multiply)