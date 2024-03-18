import Crypto.Util.number
import math
import sys
import base64
import re
import time


def compute_bit(bit_input):
    bits = math.floor(bit_input / 3)
    if len(sys.argv) > 1:
        bits = int(sys.argv[1])

    return bits


def generating_keys(bits):
    p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

    q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    while p == q:
        q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

    r = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    while r == p or r == q:
        r = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

    return p, q, r


def computation_keys(p, q, r):
    N = p * q * r
    PHI = (p - 1) * (q - 1) * (r - 1)
    e = 65537
    d = Crypto.Util.number.inverse(e, PHI)

    return N, PHI, e, d


def decimal_to_binary(CipherText):
    BinaryText = []
    for decimal_number in CipherText:
        binary_string = ""
        while decimal_number > 0:
            remainder = decimal_number % 2
            binary_string = str(remainder) + binary_string
            decimal_number //= 2
        BinaryText.append(binary_string)
    return BinaryText


def binary_to_decimal(BinaryText):
    decimal = 0
    for i, digit in enumerate(BinaryText[::-1]):
        if digit == "1":
            decimal += 2**i
    return decimal


def bitstuffX(BinaryText):
    pattern = "101"
    result = []
    for text in BinaryText:
        result.append(re.sub(pattern, pattern + "0", text))
    return result


def bitstuffY(BinaryText):
    pattern = "01"
    result = []
    for text in BinaryText:
        result.append(re.sub(pattern, pattern + "0", text))
    return result


def bitstuffZ(BinaryText):
    pattern = "1"
    result = []
    for text in BinaryText:
        result.append(re.sub(pattern, pattern + "0", text))
    return result


def format_bitstuffing(BinaryText):
    encoded_messages = []
    for word in BinaryText:
        base64_encoded = base64.b64encode(word.encode("ascii"))
        base64_message = base64_encoded.decode("ascii")
        encoded_messages.append(base64_message)

    return "MTDz".join(encoded_messages)


def format_destuff(final_encoded_messages):
    encoded_messages = final_encoded_messages.split("MTDz")
    decoded_messages = []
    for encoded_message in encoded_messages:
        base64_decoded = base64.b64decode(encoded_message)
        decoded_message = base64_decoded.decode("ascii")
        decoded_messages.append(decoded_message)

    return decoded_messages


def destuffZ(BinaryText):
    patterns = "10"
    destuff = []
    for text in BinaryText:
        destuff.append(re.sub(patterns, "1", text))
    return destuff


def destuffY(BinaryText):
    patterns = "010"
    destuff = []
    for text in BinaryText:
        destuff.append(re.sub(patterns, "01", text))
    return destuff


def destuffX(BinaryText):
    patterns = "1010"
    destuff = []
    for text in BinaryText:
        destuff.append(re.sub(patterns, "101", text))
    return destuff


def main(message):
    bits = 1024
    bit_input = bits
    p, q, r = generating_keys(bits)
    N, PHI, e, d = computation_keys(p, q, r)

    # input = "Hello World"
    input = message
    plain_text = input
    enc_st = time.time()

    CipherText = [pow(ord(c), e, N) for c in plain_text]

    BinaryText = decimal_to_binary(CipherText)

    # BitStuffing
    bitX = bitstuffX(BinaryText)
    bitY = bitstuffY(bitX)
    bitZ = bitstuffZ(bitY)

    BinaryText = bitZ

    enc_et = time.time()
    enc_elapsedTime = enc_et - enc_st

    final_encoded_messages = format_bitstuffing(BinaryText)

    decoded_message = format_destuff(final_encoded_messages)
    dec_st = time.time()

    # DeStuffing
    desZ = destuffZ(decoded_message)
    desY = destuffY(desZ)
    desX = destuffX(desY)

    BinaryText = desX

    # Convertion of Binary to Decimal
    CipherText = []
    for binary in BinaryText:
        CipherText.append(binary_to_decimal(binary))

    Decryption = [(pow(c, d, N)) for c in CipherText]
    DT = [chr(c) for c in Decryption]
    DecryptedText = "".join(DT)
    dec_et = time.time()
    dec_elapsedTime = dec_et - dec_st

    # printing

    print("\nKey Length: ", bit_input)
    print("Version: Mojisola et al.'s Version")
    print("Input: ", input)
    print("Encryption Elapsed Time:", (enc_elapsedTime * 1000), "milliseconds")
    print("Decryption Elapsed Time:", (dec_elapsedTime * 1000), "milliseconds")

    return (
        p,
        q,
        r,
        N,
        PHI,
        e,
        d,
        final_encoded_messages,
        DecryptedText,
        enc_elapsedTime,
        dec_elapsedTime,
    )
