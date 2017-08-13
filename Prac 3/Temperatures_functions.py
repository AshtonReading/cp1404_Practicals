"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def fahrenheit_to_celsius():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def celsius_to_fahrenheit():
    global fahrenheit
    fahrenheit = float(input("Fahrenheit: "))


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit_to_celsius()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        celsius_to_fahrenheit()
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")