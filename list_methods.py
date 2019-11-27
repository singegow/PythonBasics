# numbers = [2,3,5,7]
# numbers.append(20) # At the last of a list
# print(numbers)
# numbers.insert(0,30) # Insert with index to place wherever you want
# print(numbers)
# numbers.remove(3) # REmove works with the value in the list.
# print(numbers)
# numbers.clear() # Empties the whole list
# print(numbers)
# numbers = [2,3,5,7,9,12,5]
# print(numbers)
# numbers.pop() # pop be default removes the last element of a list
# print(numbers)
# numbers.pop(2) # provide the index of an element to be removed
# print(numbers)
# print(numbers.index(9)) # Used to check if a number exists in the list
# # Check for the occurrence of the element passed. Once it finds the first occurrrence it returns the index of that
# print(50 in numbers)
# print(numbers.count(5)) # count how many occurreces of passed element exists
# print(numbers.count(7))
# print(numbers.sort())
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# print(numbers2)
# numbers.append(14)
# print(numbers)
# print(numbers2)

# Exercise to remove duplicates in a list

list_num = [6,1,2,3,2,1,5,6,7,6,5,4,9,8,7]
print(list_num)
for item in list_num:
    #print("The item is " + str(item))
    count = list_num.count(item)
    #print("Count of " + str(item) + "is " + str(count))
    if count > 1:
        list_num.remove(item)
        count = count - 1
print(list_num)

# Solution from Mosh

list_num = [6,1,2,3,2,1,5,6,7,6,5,4,9,8,7]
unique = []
for item in list_num:
    if item not in unique:
        unique.append(item)
print(unique)