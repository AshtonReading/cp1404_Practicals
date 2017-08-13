name = input("Enter your name: ")
name_length = name
name_counter = 0

while name_counter in range(len(name_length)):
    if len(name_length) != 0:
        print(name[name_counter])
        name_counter= name_counter+2

    else:
        print("Please enter a valid name.")
        name = input("Enter your name: ")