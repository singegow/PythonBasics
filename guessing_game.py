# Exercise
# My code
# number_guessed = int(input("Guess: "))
#
# set_true = True
# i = 0
# while i < 3:
#     i += 1
#     if number_guessed == 9:
#         print("Yow Own")
#         break
#     else:
#         print(f"The vaue of i is {i}")
#         number_guessed = int(input("Guess: "))
# Mosh Code
secrete_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    print("The value of guess count is " + str(guess_count))
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secrete_number:
        print('You own !!')
        break
else:
    print('Sorry your failed!!!!!!!')

# While loop can be provided with else statement,
# This will eexecute if while loop doesnt ends


