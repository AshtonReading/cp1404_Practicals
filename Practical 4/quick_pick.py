import random


def generate_quick_pick():
    quick_pick = []
    for n in range(0,6):
        random_number = random.randint(1,45)
        quick_pick.append(random_number)
        # if random_number in quick_pick:
        #     random_number = random.randint(1, 45)
        #     quick_pick.append(random_number)

    quick_pick.sort()
    print(quick_pick)

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    generate_quick_pick()
