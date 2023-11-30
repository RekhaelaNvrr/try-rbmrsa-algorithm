import Crypto.Util.number 
import math
import sys

def compute_bit(bit_input):
    bits=math.floor(bit_input/3)
    if (len(sys.argv)>1):
        bits=int(sys.argv[1])
    
    return bits
        

def generating_keys(bits):
    p=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    
    q=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    while p == q:
        q=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

    r=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    while r == p or r == q:
        r=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

    return p, q, r

def computation_keys(p, q, r):
    N= p*q*r
    PHI=(p-1)*(q-1)*(r-1)
    e=65537
    d=Crypto.Util.number.inverse(e,PHI)

    return N, PHI, e, d