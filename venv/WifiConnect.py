import pywifi
from pywifi import const
import time


def wifiConnect(password, wifiName):
    wifi = pywifi.PyWiFi()
    interfaces = wifi.interfaces()[0]
    # 断开连接 注意：这个地方断开的是 WiFi 连接
    interfaces.disconnect()
    time.sleep(1)
    if interfaces.status() == const.IFACE_DISCONNECTED:
        # 测试连接 WiFi
        # 创建 WiFi 连接文件
        profile = pywifi.Profile()
        # WiFi 的名字
        profile.ssid = wifiName
        profile.key = password
        # 网卡的开放状态
        profile.auth = const.AUTH_ALG_OPEN
        # 网卡的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 删除所有的 WiFi 文件
        interfaces.remove_all_network_profiles()
        # 设定新的连接文件
        temp_profile = interfaces.add_network_profile(profile)
        # 连接新的 WiFi
        interfaces.connect(temp_profile)
        # 设置睡眠时间
        time.sleep(3)
        # 判断 WiFi 连接状态
        if interfaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False


# 读取密码本
def readPwd():
    # 读取密码本的路径，里面是密码本当中的路径
    path = ''
    file = open(path, 'r')
    while True:
        password = file.readline()
        res = wifiConnect(123, 'ccNet')
        if res:
            print('密码正确', password, end='')
            break
        else:
            print('密码错误')
    file.close()


readPwd()
