FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = " hundred "

x = 275
sx = str(x)
l1 = len(str(x))
if l1 == 1:
    print(FIRST_TEN[x-1])
elif l1 == 2:
    if sx[0] == "1":
        print(SECOND_TEN[x-10])
    else:
        if sx[1] == "0":
            print(OTHER_TENS[int(sx[0])-2])
        else:
            print(OTHER_TENS[int(sx[0])-2], FIRST_TEN[int(sx[1])-1])
elif l1 == 3:
    hu = FIRST_TEN[int(sx[0])-1] + HUNDRED
    if int(sx[1]) != 0:
        if int(sx[1]) != 1:
            hu += OTHER_TENS[int(sx[1])-2]
    elif int(sx[2])...

    print(hu)
