shop = int(input("Напиши сколько у тебя денег: "))

apple = 20
banana = 40
Berries = 60
bread = 80
chocolate = 100

if shop < apple:
    print("У тебя не достаточно денег!")
elif shop == apple:
    print("Ты можешь купить одно яблоко!")
elif shop < banana:
    print("Тебе только хватит денег на яблоки!")
elif shop == banana:
    print("Ты можешь купить один банан или два яблокa!")
elif shop < Berries:
    print("Тебе только хватит денег на банан или на яблоки!")
elif shop == Berries:
    print("Ты можешь купить одну вишню либо один банан или три яблок!")
elif shop < bread:
    print("Тебе только хватит денег на хлеб либо ягоды либо бананы или на яблоки!")
elif shop == bread:
    print("Ты можешь купить один хлеб либо два банана либо четырий яблок или одну ягоду и одно яблоко!")
elif shop < chocolate:
    print("Тебе только хватит на хлеб, вишни, банан и яблоки!")
elif shop == chocolate:
    print("Тебе только хватит денег на Шоколад либо хлеб либо ягоды либо бананы или на яблоки! ")
else:
    print("Ты можешь всё купить!")

