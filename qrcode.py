import pyqrcode
import png
qr=pyqrcode.create("{'name':'para'}")
qr.png('hello.png',scale=7)
try :
    import png
except:
    print("")
    sys.exit('0')
