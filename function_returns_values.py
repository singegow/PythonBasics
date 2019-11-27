def square(input_num):
    return input_num * input_num

result = square(3)
print(result)
print(square(4))

# If the funciton doesnt return any value then python by default uses
# return None
# None represents the absent of a value

def rect(input_num):
    print("The value passed to the rectangle:" + str(input_num))

print(rect(4)) # This print statement results "None" as we do not have any return statment defined in our funciton
