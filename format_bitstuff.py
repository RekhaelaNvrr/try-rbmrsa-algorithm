import base64

text2 = [
    "100101000011100111",
    "1100101000011100111",
    "11100101000011111001",
]

encoded_messages = []
for word in text2:
    base64_encoded = base64.b64encode(word.encode("ascii"))
    base64_message = base64_encoded.decode("ascii")
    encoded_messages.append(base64_message)

print(",".join(encoded_messages))
