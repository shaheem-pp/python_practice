# Import QRCode from pyqrcode
import random
import string
from datetime import datetime

import pyqrcode, os


def get_random_string():
    chars = string.ascii_lowercase
    strin = ''.join(random.choice(chars) for _ in range(6))
    date = datetime.now().strftime("%m%d%H%M%S")
    return 'f' + date + strin


# String which represents the QR code
s = "www.geeksforgeeks.org"

# Generate QR code
url = pyqrcode.create(s)

file_name = get_random_string() + ".png"

# Create and save the png file naming "myqr.png"

url.png(file_name, scale = 6)
