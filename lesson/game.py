import random

user = ''
computer = random.randint(1, 10)
# print(computer)
print("    GAME STARTED")
tries = 1

while tries < 4: # Роботает только когда '< 2'.
    user = int(input("Guess a number, 1-10: "))
    if user == computer:
        print("You're Good!")
        break
    elif user < computer:
        print("Input a bigger number")
    elif user > computer:
        print("Input a smaller number")
    tries = tries + 1
if user == computer:
    print(f"You won with {tries} try")
    print("£50000- was taken from your credit card for playing this game")
    print("НЕ ИГРАЙ АЗАРТНЫЕ ИГРЫ!!!")
else:
    print(f"Computer chosed {computer}")

