import onvif_py
import time

self = onvif_py.Onvif_hik(ip = "192.168.1.30", port = "8080", username = "admin", password = "abcd1234", wsdl = "C:\Program Files\Python310\Lib\site-packages\onvif_zeep-0.2.12-py3.10.egg\Lib\site-packages\wsdl")
if self.content_cam() == True :
    print('go to preset 1')
    self.goto_preset(1)
    time.sleep(5)
    start = time.time()
    for i in range(1,10):
        self.Snapshot()
    end = time.time()
    print('time usage: ', (end - start) * 100, 'ms')
    print('go to preset 2')
    self.goto_preset(2)
    time.sleep(5)
    start = time.time()
    for i in range(1,10):
        self.Snapshot()
    end = time.time()
    print('time usage: ', (end - start) * 100, 'ms')
else :
    print("fail!")
