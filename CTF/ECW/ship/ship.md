# Netcat

So when connecting to the challenge with have a lot of output.
I redirect it to nc.log
We can see some base64 pattern.

# Script

So I write a little python3 that search and decode any base64 strings.

```python
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
```

# Flag

Lanch it and grep :

```bash
python3 extract.py | strings | grep "ECW"
Decoded Data: ECW{ECW2024_NmEa_Flag}
```
