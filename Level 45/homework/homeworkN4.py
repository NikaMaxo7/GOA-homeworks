def calc(s):
    total1 = ""
    for i in s:
        if i == "A":
            total1 += "65"
        elif i == "B":
            total1 += "66"
        elif i == "C":
            total1 += "67"
        elif i == "D":
            total1 += "68"
        elif i == "E":
            total1 += "69"
        elif i == "F":
            total1 += "70"
        elif i == "G":
            total1 += "71"
        elif i == "H":
            total1 += "72"
        elif i == "I":
            total1 += "73"
        elif i == "J":
            total1 += "74"
        elif i == "K":
            total1 += "75"
        elif i == "L":
            total1 += "76"
        elif i == "M":
            total1 += "77"
        elif i == "N":
            total1 += "78"
        elif i == "O":
            total1 += "79"
        elif i == "P":
            total1 += "80"
        elif i == "Q":
            total1 += "81"
        elif i == "R":
            total1 += "82"
        elif i == "S":
            total1 += "83"
        elif i == "T":
            total1 += "84"
        elif i == "U":
            total1 += "85"
        elif i == "V":
            total1 += "86"
        elif i == "W":
            total1 += "87"
        elif i == "X":
            total1 += "88"
        elif i == "Y":
            total1 += "89"
        elif i == "Z":
            total1 += "90"
        elif i == "a":
            total1 += "97"
        elif i == "b":
            total1 += "98"
        elif i == "c":
            total1 += "99"
        elif i == "d":
            total1 += "100"
        elif i == "e":
            total1 += "101"
        elif i == "f":
            total1 += "102"
        elif i == "g":
            total1 += "103"
        elif i == "h":
            total1 += "104"
        elif i == "i":
            total1 += "105"
        elif i == "j":
            total1 += "106"
        elif i == "k":
            total1 += "107"
        elif i == "l":
            total1 += "108"
        elif i == "m":
            total1 += "109"
        elif i == "n":
            total1 += "110"
        elif i == "o":
            total1 += "111"
        elif i == "p":
            total1 += "112"
        elif i == "q":
            total1 += "113"
        elif i == "r":
            total1 += "114"
        elif i == "s":
            total1 += "115"
        elif i == "t":
            total1 += "116"
        elif i == "u":
            total1 += "117"
        elif i == "v":
            total1 += "118"
        elif i == "w":
            total1 += "119"
        elif i == "x":
            total1 += "120"
        elif i == "y":
            total1 += "121"
        elif i == "z":
            total1 += "122"

    total2 = total1.replace("7", "1")

    sum_total1 = sum(int(x) for x in total1)
    sum_total2 = sum(int(x) for x in total2)

    return sum_total1 - sum_total2