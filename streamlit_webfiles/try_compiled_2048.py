# based on: https://repl.it/@billbuchanan/getprimen
# based on: https://repl.it/@billbuchanan/getprimen
# Source: extendedeuclideanalgorithm.com
import time
import Crypto.Util.number
import math
import sys
import random as random
import re
import base64


def compute_bit(bit_input):
    bits = math.floor(bit_input / 4)
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

    s = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    while s == p or s == q or s == r:
        s = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

    return p, q, r, s


def gen_e(PHI):
    e = random.randint(2, 1000000)
    while math.gcd(e, PHI) != 1:
        e = random.randint(2, 1000000)
    return e


def computation_keys(p, q, r, s):
    N = p * q * r * s
    PHI = (p - 1) * (q - 1) * (r - 1) * (s - 1)
    e = gen_e(PHI)

    return N, PHI, e


# Warning: can't handle b=0. See extendedeuclideanalgorithm.com/code for a version that can
def gcd_iterative(a, b):
    """Calculating the greatest common divisor
    using the Euclidean Algorithm (non-recursive)
    (Source: extendedeuclideanalgorithm.com/code)
    """

    # Set default values for the quotient and the remainder
    q = 0  # CONSTANT-- DON'T CHANGE
    r = 1  # CONSTANT-- DON'T CHANGE

    """
	In each iteration of the loop below, we
	calculate the new quotient, remainder, a and b.
	r decreases, so we stop when r = 0 
	"""
    while r > 0:
        # The calculations
        q = math.floor(a // b)
        r = a - q * b

        # The values for the next iteration
        a = b
        b = r if (r > 0) else b

    return abs(b)


# Can handle b=0
def gcd_iterative_2(a, b):
    """Calculating the greatest common divisor
    using the Euclidean Algorithm (non-recursive)
    (Source: extendedeuclideanalgorithm.com/code)
    """

    # Set default values for the quotient and the remainder
    q = 0
    r = 1

    """
    In each iteration of the loop below, we
    calculate the new quotient, remainder, a and b.
    r decreases, so we stop when r = 0 
    """
    while b > 0:
        # The calculations
        q = math.floor(a // b)
        r = a - q * b

        # The values for the next iteration
        a = b
        b = r

    return abs(a)


def gcd(a, b):
    """Calculating the greatest common divisor
    using the Euclidean Algorithm (recursive)
    (Source: extendedeuclideanalgorithm.com/code)
    """
    if b == 0:
        return abs(a)

    q = math.floor(a // b)
    r = a - q * b
    return abs(b) if (r == 0) else gcd(b, r)


# Warning: this version can't handle b=0. See extendedeuclideanalgorithm.com/code for a version that can.
def xgcd_iterative(a, b):
    """Calculates the gcd and Bezout coefficients,
    using the Extended Euclidean Algorithm (non-recursive).
    (Source: extendedeuclideanalgorithm.com/code)
    """
    # Set default values for the quotient, remainder,
    # s-variables and t-variables
    q = 0
    r = 1
    s1 = 1
    s2 = 0
    s3 = 1
    t1 = 0
    t2 = 1
    t3 = 0

    """
	In each iteration of the loop below, we
	calculate the new quotient, remainder, a, b,
	and the new s-variables and t-variables.
	r decreases, so we stop when r = 0
	"""
    while r > 0:
        # The calculations
        q = math.floor(a // b)
        r = a - q * b
        s3 = s1 - q * s2
        t3 = t1 - q * t2

        """
		The values for the next iteration, 
		(but only if there is a next iteration)
		"""
        if r > 0:
            a = b
            b = r
            s1 = s2
            s2 = s3
            t1 = t2
            t2 = t3

    return abs(b), s2, t2


# Can handle b=0
def xgcd_iterative_2(a, b):
    """Calculates the gcd and Bezout coefficients,
    using the Extended Euclidean Algorithm (non-recursive).
    (Source: extendedeuclideanalgorithm.com/code)
    """
    # Set default values for the quotient, remainder,
    # s-variables and t-variables
    q = 0
    r = 1
    s1 = 1
    s2 = 0
    s3 = 1
    t1 = 0
    t2 = 1
    t3 = 0

    """
    In each iteration of the loop below, we
    calculate the new quotient, remainder, a, b,
    and the new s-variables and t-variables.
    r decreases, so we stop when r = 0
    """
    while b > 0:
        # The calculations
        q = math.floor(a // b)
        r = a - q * b
        s3 = s1 - q * s2
        t3 = t1 - q * t2

        """
        The values for the next iteration, 
        (but only if there is a next iteration)
        """

        a = b
        b = r
        s1 = s2
        s2 = s3
        t1 = t2
        t2 = t3

    return abs(a), s1, t1


def xgcd(a, b, s1=1, s2=0, t1=0, t2=1):
    """Calculates the gcd and Bezout coefficients,
    using the Extended Euclidean Algorithm (recursive).
    (Source: extendedeuclideanalgorithm.com/code)
    """
    if b == 0:
        return abs(a), 1, 0

    q = math.floor(a // b)
    r = a - q * b
    s3 = s1 - q * s2
    t3 = t1 - q * t2

    # if r==0, then b will be the gcd and s2, t2 the Bezout coefficients
    return (abs(b), s2, t2) if (r == 0) else xgcd(b, r, s2, s3, t2, t3)


def gcd_checker(e, PHI):
    a = e
    b = PHI
    my_gcd, s, t = xgcd(a, b)
    verification = abs(s * a + t * b)
    while my_gcd != verification:
        gen_e()
        a = e
        b = PHI
        my_gcd, s, t = xgcd(a, b)
        verification = abs(s * a + t * b)
    return s, t


def generating_d(x, y, e, PHI):
    a = e
    b = PHI

    eea_d = (PHI * x) + (e * y)

    if eea_d == gcd(a, b):
        d = y
        if d > PHI:
            d = d % PHI
        elif d < 0:
            d = d + PHI

        return d
    else:
        print("error")


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


def crt_equations(p, q, r, s, N, d):
    dp = d % (p - 1)
    dq = d % (q - 1)
    dr = d % (r - 1)
    ds = d % (s - 1)

    return dp, dq, dr, ds


def modinv(a, m):
    """Calculate the modular inverse of a modulo m."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# Calculate modular inverses
def modInv_Computation(N, p, q, r, s):
    pInv = modinv(N // p, p)
    qInv = modinv(N // q, q)
    rInv = modinv(N // r, r)
    sInv = modinv(N // s, s)

    return pInv, qInv, rInv, sInv


def four_parts(CipherText, p, q, r, s, N, pInv, qInv, rInv, sInv, dp, dq, dr, ds):
    message = []
    for text in CipherText:
        M1 = pow(text, dp, p) * q * r * s * pInv
        M2 = pow(text, dq, q) * p * r * s * qInv
        M3 = pow(text, dr, r) * p * q * s * rInv
        M4 = pow(text, ds, s) * p * q * r * sInv
        final_CT = (M1 + M2 + M3 + M4) % N
        message.append(final_CT)
    return message


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


def format_destuff(final_encoded_messages):
    encoded_messages = final_encoded_messages.split("MTDz")
    decoded_messages = []
    for encoded_message in encoded_messages:
        base64_decoded = base64.b64decode(encoded_message)
        decoded_message = base64_decoded.decode("ascii")
        decoded_messages.append(decoded_message)

    return decoded_messages


def main(input):
    bits = 2048
    bit_input = bits
    p, q, r, s = generating_keys(bits)
    N, PHI, e = computation_keys(p, q, r, s)

    y, x = gcd_checker(e, PHI)
    d = generating_d(x, y, e, PHI)

    input = input
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

    pInv, qInv, rInv, sInv = modInv_Computation(N, p, q, r, s)
    dp, dq, dr, ds = crt_equations(p, q, r, s, N, d)
    Decryption = four_parts(
        CipherText, p, q, r, s, N, pInv, qInv, rInv, sInv, dp, dq, dr, ds
    )
    DT = [chr(c) for c in Decryption]
    DecryptedText = "".join(DT)
    dec_et = time.time()
    dec_elapsedTime = dec_et - dec_st

    # printing

    print("\nKey Length: ", bit_input)
    print("Version: TRY's Version")
    print("Input: ", input)
    print("Encryption Elapsed Time:", (enc_elapsedTime * 1000), "milliseconds")
    print("Decryption Elapsed Time:", (dec_elapsedTime * 1000), "milliseconds")
    print("\x1b[32m\n\nDecrypted Message:\x1b[1m " + DecryptedText, "\x1b[0m")
    print("\n\n")

    return (
        p,
        q,
        r,
        s,
        N,
        PHI,
        e,
        d,
        final_encoded_messages,
        DecryptedText,
        enc_elapsedTime,
        dec_elapsedTime,
    )
