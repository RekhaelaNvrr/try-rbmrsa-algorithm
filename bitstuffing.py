import re


def bitstuffX(text):
    pattern = "101"
    result = re.sub(pattern, pattern + "0", text)
    return result


def bitstuffY(text):
    pattern = "01"
    result = re.sub(pattern, pattern + "0", text)
    return result


def bitstuffZ(text):
    pattern = "1"
    result = re.sub(pattern, pattern + "0", text)
    return result


def main():
    text = '100101000011100111' #example only
    bitX = bitstuffX(text)
    bitY = bitstuffY(bitX)
    bitZ = bitstuffZ(bitY)
    print(bitX)
    print(bitY)
    print("Final Bit-stuffed: ", bitZ)


main()
