import base64
import format_bitstuff

encoded_messages = format_bitstuff.final_encoded_messages.split("//")
decoded_messages = []

for encoded_message in encoded_messages:
    base64_decoded = base64.b64decode(encoded_message)
    decoded_message = base64_decoded.decode("ascii")
    decoded_messages.append(decoded_message)

# Printing decoded messages
print("\nDecoded Messages:", decoded_messages)
