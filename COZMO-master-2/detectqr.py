from pyzbar.pyzbar import decode
from PIL import Image
def decodeQR(): 
    # res = decode(Image.open('main.png'))
    # res = decode(Image.open('paracetamol.png'))
    # res = decode(Image.open('aspirin.png'))
    # res = decode(Image.open('morphine.png'))
    res = decode(Image.open('outA.png'))
    print(res)
    print(type(res))
    if res:
        for i in res:
            return i.data
    else:
        return res