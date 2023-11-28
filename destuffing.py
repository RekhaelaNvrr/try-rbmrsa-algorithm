import re


def destuffZ(text):
    patterns = "10"
    deStuff = re.sub(patterns, "1", text)
    return deStuff


def destuffY(text):
    patterns = "010"
    deStuff = re.sub(patterns, "01", text)
    return deStuff


def destuffX(text):
    patterns = "1010"
    deStuff = re.sub(patterns, "101", text)
    return deStuff


def main():
    text = '1000100010000001001010001001010' #example only
    desZ = destuffZ(text)
    desY = destuffY(desZ)
    desX = destuffX(desY)
    print(desZ)
    print(desY)
    print("Final Destuffed: ", desX)


main()
