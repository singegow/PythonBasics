def welcome(first_name, last_name):
    print("Hello Dear " + str(first_name) + str(last_name))
    print("Welcome !!!!!!!")


print("start")
welcome("Anitha", "Ramu")
welcome("Ramu", "Anitha") # Positional arguments
welcome(last_name="Ramu", first_name="anitha") # Keywork arguments
print("Finish")

# parameters are the placeholder in a function for receiving information == > name is a parameter
# argument is actual piece of infomation which we supply to a function ==> "John" is an argument
# Two types of arguments, positional arguments and keyword arguments
# welcome("Anitha", "Ramu") ==> Positional arguments
# welcome("Anitha", first_name="Ramu") ==> Key word arguments
# If you are mixing positional and keywork arguments, make sure positional arguments are always first and keyword
# arguments are placed at the end

