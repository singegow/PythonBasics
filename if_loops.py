# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's hot day")
#     print("Drink plent of water")
# elif is_cold:
#     print("Its a cold day")
#     print("Wear warm clothes")
# else:
#     print("Its a lovely day")
# print("Enjoy your day")
house_price = 100
has_good_credict = False
if has_good_credict:
    print("will put down by 10%")
else:
    print("will put down by 20%")
print(house_price)
print(f"Down paytment is : {house_price}")
#print("Down payment is " + house_price)
# The above line will fail. due to type mismatch
# But in case of formatted string. its handled internally
print("Down payment is " + str(house_price))


