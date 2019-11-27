# # For loops for iteration
# # In python list can be defined using []
# # A list is a collection of itemps. list of anything
# for item in 'Pthon':
#     print(item)
#
# for itemps in ['Anitha', 'Alekha', 'Ashwini']:
#     print(itemps)
#
# for item in [1,2,3,4,5]:
#     print(item)
#
# # range = function  creates an object. its not an list.
# # Its a special type of object, which we can iterate over
# # In each iteration it will spit out a new number
# # range(10) = means 10 not inclueded, only till 9
#
# for item in range(10):
#     print(item)
#
# for item in range(5,10):
#     print(item)

# range function can also accepts , step at the end.
# If we have a range (5,10,2) - > the range wil increment 5 by 2 and stores the number till they are under 10

# Exercise
total_price = int()
print(total_price)
prices = [10, 20, 30, 40, 50, 60, 70]
for items in prices:
    total_price += int(items)
    print(items)
print(f"The total price is {total_price}")