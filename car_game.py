# user_input = ""
#
# while user_input.lower() != "quit":
#     user_input = input("> ")
#     if user_input == "help":
#         print("Displayng helath mendu")
#     elif user_input.lower() == "start":
#         print("Car started")
#     elif user_input.lower() == "stop":
#         print("car stopped")
#     else:
#         print("Not valid input")
# else:
#     print("User entered Quit. So quitting the game")

# better to call lower while getting user input. rather than in all conditions
# command = input("> ").lower()
# The above code will print "Not valid input" Though we provide quit. which is valid..
# We can fix this by making while True and breaking the loop as soon as we get proper iquit statement

user_input = ""
car_started = False
car_stopped = False

while True:
    user_input = input("> ").lower()
    if user_input == "help":
        print("""
Start - to start the car
Stop - to stop the car
quit - quit        
        """)
    elif user_input.lower() == "start":
        if car_started:
            print("Car already started")
        else:
            print("Car started")
            car_started = True
    elif user_input.lower() == "stop":
        if car_stopped:
            print("Car already stopped")
        else:
            print("Car stopped")
            car_stopped = True
    elif user_input == "quit":
        break
    else:
        print("Not valid input")