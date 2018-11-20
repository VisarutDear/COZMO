import pyqrcode
import png
qr=pyqrcode.create(""name":"DEAR", "age":18, "city":"Bangkok", "medname":"TYLENOL","amount":"1","time":"12:00"")
qr.png('hello.png',scale=7)
try :
    import png
except:
    print("")
    sys.exit('0')
