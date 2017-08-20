numbers = []

while len(numbers) <5:
    number = int(input("Enter a number: "))
    numbers.append(number)

print(numbers)
print("The first number is {}" .format(numbers[0]))
print("The last number is {}" .format(numbers[4]))
print("The smallest number is {}" .format(int(min(numbers))))
print("The largest number is {}" .format(int(max(numbers))))
print("The average of the numbers is {}" .format(sum(numbers) / len(numbers)))
