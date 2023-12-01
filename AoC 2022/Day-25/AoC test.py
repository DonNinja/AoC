values = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
keys = {2: "2", 1: "1", -1: "-", -2: "="}

file = open("input25.txt")


def Decode(text: str):
    dec = 0
    for ind in range(len(text)):
        calc = 5**ind * values[text[::-1][ind]]
        dec += calc

    return dec


def Encode(number: int):
    # *The number needs to go closer towards zero the further we go,
    # *it is currently just jumping between 2 numbers when trying to encode 314159265
    text = ""
    prevIndex = 0
    while number != 0:
        Index = 0
        temp = 1
        oldTemp = temp

        keyVal = 0
        while temp * 2 < abs(number):
            Index += 1
            temp *= 5

            if temp + oldTemp >= abs(number):
                keyVal = 1
            elif temp * 2 + oldTemp >= abs(number):
                keyVal = 2

            oldTemp = temp

        text += "0" * (prevIndex - (Index + 1))

        removal = 0

        if keyVal != 0:
            removal = temp * keyVal
        else:
            removal = number

        if number > 0:
            if keyVal != 0:
                text += keys[keyVal]
            else:
                text += keys[number]
            number -= removal
        elif number < 0:
            if keyVal != 0:
                text += keys[-keyVal]
            else:
                text += keys[-number]
            number += removal

        prevIndex = Index

    # Add zeroes to the end if there should be any
    if prevIndex > 0:
        text += "0" * prevIndex

    return text


total = 0
for line in file.readlines():
    total += Decode(line.strip())

# print(Decode("1121-1110-1=0"))
print(Encode(25))
