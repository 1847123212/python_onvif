import onvif_py
import time

self = onvif_py.Onvif_hik(ip = "192.168.1.44", port = 80, username = "onvif", password = "abcd1234", wsdl = "'C:\Program Files\Python310\Lib\site-packages\onvif_zeep-0.2.12-py3.10.egg\Lib\site-packages\wsdl'")
if self.content_cam() == True :
    start = time.time()
    for i in range(1,10):
        self.Snapshot()
    end = time.time()
    print('time usage: ', (end - start) * 1000 / 10, 'ms')
else :
    print("fail!")
