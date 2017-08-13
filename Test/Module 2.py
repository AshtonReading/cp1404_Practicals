i = 1
while i <= 10:
    print(i)
    i += 2.5
print("Finished\n")

shopping = ["milk", "bread", "cheese", "ham"]
print(shopping[3])
print(shopping[2])
print(shopping[1])
print(shopping[0])
for motto in shopping:
    print(motto + "!")

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

for chicken in range(5):
    print("A whole lotta chickens")

list = [1, 1, 2, 3, 5, 8, 13]
print(list[4])

list = [1, 2, 3]
for var in list:
    print(var)