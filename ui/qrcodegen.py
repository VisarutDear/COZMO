import pyqrcode
import png
import json

with open('data.json') as f:
    data = json.load(f)

qr=pyqrcode.create(str(data[-1]))
qr.png('qrcode.png',scale=7)
