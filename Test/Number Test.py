secret_number = print(int(input("Guess the Secret Number from 1 ro 10: ")))
#x= print(int(input("Enter a number: ")))
while secret_number != 6:
    print("Guess Again!")
    secret_number = int(input("Guess the Secret Number from 1 ro 10: "))

print("Correct! It was 6!")