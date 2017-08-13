
def main():
    name, name_counter, name_length = get_name()

    name_slicing(name, name_counter, name_length)


def name_slicing(name, name_counter, name_length):
    i = int(input("Enter how many characters you want to skip: "))
    while name_counter in range(len(name_length)):
        if len(name_length) != 0:
            print(name[name_counter])
            name_counter = name_counter + i

        else:
            print("Please enter a valid name.")
            name = input("Enter your name: ")


def get_name():
    name = input("Enter your name: ")

    name_length = name
    name_counter = 0
    return name, name_counter, name_length


main()