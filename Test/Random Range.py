import random
from random import *

number_of_times = int(input("How many numbers: "))

for i in range(number_of_times):
    x = randint(1, 10)
    print(i,x)
    if x < 5:
        print("low")
    else:
        print("high")