# numbers = [3, 1, 4, 1, 5, 9, 2]
#
# numbers.append(1)
# numbers.insert(0,"ten")
#
# print(numbers)
# print(numbers[2:])
#
# print(9 in numbers)


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month {} : " .format(month)))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()