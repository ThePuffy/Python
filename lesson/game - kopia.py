import random

computer = random.randint(1, 10)
print("    GAME STARTED")
user = int(input("Guess a number, 1-10: "))

tries = 0

while tries < 3:
    if user == computer:
        print("You're Good!")
        break
    elif user < computer:
        print("Input a bigger number")
        user = int(input("Guess a number, 1-10: "))
    elif user > computer:
        print("Input a smaller number")
        user = int(input("Guess a number, 1-10: "))
    tries = tries + 1
if tries == 3:
    print(f"You have used all of the {tries} tries")

# Доделать!