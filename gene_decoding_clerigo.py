name = input("Enter your name:")
random = ""

for x in range(len(name)):
    char = name[x]

    if char == "A":
        random += "B"
    elif char == "B":
        random += "C"
    elif char == "C":
        random += "D"
    elif char == "D":
        random += "E"
    elif char == "E":
        random += "F"
    elif char == "F":
        random += "G"
    elif char == "G":
        random += "H"
    elif char == "H":
        random += "I"
    elif char == "I":
        random += "J"
    elif char == "J":
        random += "K"
    elif char == "K":
        random += "L"
    elif char == "L":
        random += "M"
    elif char == "M":
        random += "N"
    elif char == "N":
        random += "O"
    elif char == "O":
        random += "P"
    elif char == "P":
        random += "Q"
    elif char == "Q":
        random += "R"
    elif char == "R":
        random += "S"
    elif char == "S":
        random += "T"
    elif char == "T":
        random += "U"
    elif char == "U":
        random += "V"
    elif char == "V":
        random += "W"
    elif char == "W":
        random += "X"
    elif char == "X":
        random += "Y"
    elif char == "Y":
        random += "Z"
    elif char == "Z":
        random += "A"
    else:
        random += char
        
print(random)
