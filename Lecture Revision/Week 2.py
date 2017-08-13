mobile_number = "0431043405"
name = "Ashton Reading"

print(name[2])
print(name[-1])
print(name[0:6])



new_word = name[5].upper() + name[8:]
print(new_word)

new_name = name[1].upper() + name[2] + name[8] + name[-2] + name[0].lower()
print(new_name)

print(len(name))

#phone_number = input("Mobile Number: ")
#if not phone_number.startswith("04"):
   # print("Let me stop you right there")

mname = "Monty"
money = 73.6

print(mname + " has " + "{:.2f}".format(money))

