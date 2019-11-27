names = ['anitha', 'alekha', 'ashwini']
print(names)
print(names[2])
print(names[-1])
print(names[-2])
print(names[1:])
print(names[:2])
print(names[:])
names[0] = "ANOITHA"
print(names)

# Exercise
numbers = [300,2,5,6,12,9,20,45]
largest_num = numbers[0]
# The above apporach also will work and below one also
# largest_num = 0
for num in numbers:
    if(num > largest_num):
        largest_num = num
print(f"The Largest number is {largest_num}")

