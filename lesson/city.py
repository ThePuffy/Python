city = input("Input a city: ").lower()

while True:
    city1 = input("Input a city: ").lower()
    if city[-1] != city1[0]:
        print("The game Stopped")
        break
    city = city1
