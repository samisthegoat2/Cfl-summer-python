import random

while True:
    roll = random.randint(1,6)
    print(f"Number rolled is:{roll}")

    if roll == 6:
        print(f"correct number:6")
        break
 
