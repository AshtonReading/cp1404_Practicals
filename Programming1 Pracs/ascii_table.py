
LOWER = 33
UPPER = 127

# user_character = input("Enter a Character: ")
# print("The ASCII code for", user_character, "is:", ord(user_character))
#
# user_number = (int(input("Enter a number between {} and {}: " .format(LOWER, UPPER))))
# while user_number< LOWER or user_number> UPPER:
#     print("Enter a valid number")
#     user_number = (int(input("Enter a number between 33 and 127: ")))
#
# print("The character for", user_number, "is:", chr(user_number))


for count in range(33,127):
    print( "{:<6} {}" .format(count, chr(count)))