import base64
import re

# Open the file
with open('nc.log', 'r') as file:
    content = file.read()

# Base64 regex
base64_strings = re.findall(r'[A-Za-z0-9+/=]{8,}', content)

# Decode each Base64 string and print the result
for b64_str in base64_strings:
    try:
        decoded_data = base64.b64decode(b64_str).decode('utf-8')
        print(f"Base64 String: {b64_str}")
        print(f"Decoded Data: {decoded_data}")
    except Exception as e:
        print(f"Error decoding {b64_str}: {e}")
