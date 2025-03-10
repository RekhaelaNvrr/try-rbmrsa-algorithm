from bitstuffing import bitstuffX, bitstuffY, bitstuffZ
from destuffing import destuffZ, destuffY, destuffX
from format_bitstuff import format_bitstuffing
from format_destuff import format_destuff
from generating_keys import generating_keys, computation_keys, compute_bit
from binary_conversion import decimal_to_binary, binary_to_decimal

print("\n ----------")
print("RBMRSA Avalanche Checker Version:")
print("\n Key bit-length: 1024")
original_plaintext = input("\tEnter a phrase/text: ")
modified_plaintext = input("\tChange 1 part of the text/phrase: ")

#Algorithm keys -------
bit_input = 1024
bits = compute_bit(bit_input)

(
    p,
    q,
    r,
) = generating_keys(bits)

N, PHI, e, d = computation_keys(p, q, r)

# Encryption of text message
original_ciphertext = [pow(ord(c), e, N) for c in original_plaintext]

# Conversion of Decimal to Binary
Original_BinaryText = decimal_to_binary(original_ciphertext)

# BitStuffing
bitX = bitstuffX(Original_BinaryText)
bitY = bitstuffY(bitX)
bitZ = bitstuffZ(bitY)

Original_BinaryText = bitZ 

#Modified text -----------------------------------------
#Algorithm keys -------
bits = compute_bit(bit_input)

(
    p,
    q,
    r,
) = generating_keys(bits)

N, PHI, e, d = computation_keys(p, q, r)

# Encryption of text message
modified_ciphertext = [pow(ord(c), e, N) for c in modified_plaintext]

# Conversion of Decimal to Binary
Modified_BinaryText = decimal_to_binary(modified_ciphertext)

# BitStuffing
bitX = bitstuffX(Modified_BinaryText)
bitY = bitstuffY(bitX)
bitZ = bitstuffZ(bitY)

Modified_BinaryText = bitZ

# Calculating Avalanche Effect (Bitwise XOR)
def compute_avalanche_effect(Original_BinaryText, Modified_BinaryText):
    total_bits = 0
    changed_bits = 0
    
    # Iterate through each pair of original and modified ciphertexts
    for original, modified in zip(Original_BinaryText, Modified_BinaryText):
        # Convert ciphertexts to binary strings
        original_int = int(original, 2)
        modified_int = int(modified, 2)
        
        # Count the total number of bits
        total_bits += len(original)
        
        # Count the number of changed bits
        changed_bits += bin(original_int ^ modified_int).count('1')
                
    # Calculate the percentage of changed bits
    avalanche_percentage = (changed_bits / total_bits) * 100
    return avalanche_percentage, changed_bits, total_bits

avalanche_percentage, changed_bits, total_bits = compute_avalanche_effect(Original_BinaryText, Modified_BinaryText)
print("\nchanged bits:",  changed_bits)
print("total bits:",  total_bits)
print("\nAvalanche Effect: {:.2f}%".format(avalanche_percentage))
print("---- end ----\n")