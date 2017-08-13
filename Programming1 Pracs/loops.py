

for i in range(1, 21, 2):
 print(i, end=' ')
print()

#a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100

for i in range(0,101,10):
    print(i, end= " ")
print()

#b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

for i in range(20, -1, -1):
    print(i, end=" ")
print()
#Add a loop to the sales bonus exercise you did above, so that the program repeatedly asks for the
#user's sales and prints the bonus until they enter a negative number.
#Remember that until is the opposite of while.


sales = float(input("Enter sales: $"))
while sales >-1:

    if sales > 999:
       bonus = sales*0.15
       print("Your Bonus is: ", bonus)

    else:
       bonus = sales*0.1
       print("Your Bonus is: ", bonus)
    sales = float(input("Enter sales: $"))
else:
    print("Negative Number given")