# import qrtools
# qr = qrtools.QR()
# qr.decode("expic.jpg")
# print(qr.data)


from pyzbar.pyzbar import decode
from PIL import Image
res = decode(Image.open('DEAR.JPG'))
if res:
    for i in res:
        print(i.data)
else:
    print("no no")