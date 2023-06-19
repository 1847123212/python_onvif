from onvif import ONVIFCamera
import zeep
import time
import requests
from requests.auth import HTTPDigestAuth
import os

class Onvif_hik(object):
    def __init__(self, ip: str, port: int, username: str, password: str, wsdl: str):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.wsdl = wsdl
        zeep.xsd.simple.AnySimpleType.pythonvalue = self.zeep_pythonvalue
        self.save_path = "{}\T{}.jpg".format(os.getcwd(), str(time.time()))  # 截图保存路径
        print("cam ip:", self.ip, ":", self.port, "username:", self.username, "password:", self.password, "wsdl:", self.wsdl, "save_path:", self.save_path)

    def content_cam(self):
        """
        链接相机地址
        :return:
        """
        try:
            self.mycam = ONVIFCamera(self.ip, self.port, self.username, self.password, self.wsdl) # WSDL文件目录不同的操作系统以及安装目录是不一样的，注意替换
            self.media = self.mycam.create_media_service()  # 创建媒体服务
            self.media_profile = self.media.GetProfiles()[0]  # 获取配置信息
            self.ptz = self.mycam.create_ptz_service()  # 创建控制云台服务
            return True
        except Exception as e:
            return False

    def Snapshot(self):
        """
        截图
        :return: 
        """
        res = self.media.GetSnapshotUri({'ProfileToken': self.media_profile.token})
        response = requests.get(res.Uri, auth=HTTPDigestAuth(self.username, self.password))
        with open(self.save_path, 'wb') as f:  # 保存截图
            f.write(response.content)

    def get_presets(self):
        """
        获取预置点列表
        :return:预置点列表--所有的预置点
        """
        presets = self.ptz.GetPresets({'ProfileToken': self.media_profile.token})  # 获取所有预置点,返回值：list
        return presets

    def goto_preset(self, presets_token: int):
        """
        移动到指定预置点
        :param presets_token: 目的位置的token，获取预置点返回值中
        :return: 
        """
        try:
            self.ptz.GotoPreset(
                {'ProfileToken': self.media_profile.token, "PresetToken": presets_token})  # 移动到指定预置点位置
        except Exception as e:
            print(e)
 
    def zeep_pythonvalue(self, xmlvalue):
        return xmlvalue
