user_input = input(">")
message = user_input.split(' ')
print(message)
emojis = {
    ":)" : "HAPPY FACE",
    ":(" : "SAD FACE"
}
output_string = ""
for item in message:
    output_string += emojis.get(item, item) + ' '
print(output_string)
