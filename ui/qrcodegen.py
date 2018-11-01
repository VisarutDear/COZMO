import pyqrcode
import png
import json
from PIL import Image

def generate():
    with open('data.json') as f:
        data = json.load(f)

    qr = pyqrcode.create(str(data[-1]))
    qr.png('qrcode.png',scale=7)

    qr = Image.open('C:/wamp64/www/cozmo_ui/qrcode.png')
    qr.save('C:/wamp64/www/cozmo_ui/static/qrcode.png')
# line 14: save QRCODE to static folder
# After run this code there will be TWO qrcode.png (1. at the same directory as this .py file 2. in static folder)
