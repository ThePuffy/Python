vowels = "aeiouy"
example = "hieeelal aooo"
stringo = ""
stable = {"Type":"","index":None}

for indexo, i in enumerate(example):
    if i in vowels:
        print(i,"is a vowel")
    elif i == " ":
        print(i,"is a space")
    else:
        print(i,"is a consonant")
        stringo += i
        stable["Type"] = "consonant"
        stable["index"] = indexo