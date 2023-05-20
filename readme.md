# python-onvif-zeep
ONVIF Client Implementation in Python3

# Dependencies
    zeep >= 3.0.0

# Install python-onvif-zeep
install with pip3

    pip install --upgrade onvif_zeep
after install,  you can find：

    onvif-zeep 0.2.12
when you run：

    pip list
Pls make sure this python code donot support **onvif2-zeep 0.3.4**!!!


# Geting start

    from onvif import ONVIFCamera
    mycam = ONVIFCamera('ip addr', 'port', 'onvif_username', 'onvif_passwd', '/etc/onvif/wsdl/')

all operations defined in the WSDL document, so make sure the right wsdl content, especially in windows.