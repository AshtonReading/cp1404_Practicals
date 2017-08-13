
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid Number of Items!")
    number_of_items = int(input("Number of items: "))

total_cost = 0


for i in range(number_of_items):
    total_cost = total_cost + float(input("Price of item: $"))


if total_cost > 100:
    discount = total_cost * 0.9
    print("Total price for", number_of_items, "items: $", format(discount, '.2f'))
else:
    print("Total price for", number_of_items, "items: $", format(total_cost, '.2f'))
