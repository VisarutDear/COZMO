import pyqrcode
import png
import json
from PIL import Image

with open('data.json') as f:
    data = json.load(f)

qr = pyqrcode.create(str(data[-1]))
qr.png('qrcode.png',scale=7)

qr = Image.open('C:/wamp64/www/cozmo_ui/qrcode.png')
qr.save('C:/wamp64/www/cozmo_ui/templates/static/qrcode.png')
