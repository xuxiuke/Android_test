
#服务器地址
class serverAddress(object):

    def getAddress(self):
        serverAddress=[]
        #serveraddress1 = "https://iotus.wuliancloud.com:443/"
        serveraddress1 = "https://iotsh.wuliancloud.com:443/"
        #serveraddress1 = "https://iotbj.wuliancloud.com:443/"
        serveraddress2 = "https://testv6.wulian.cc/"
        serveraddress3 = "https://testv2.wulian.cc:50090/"
        serveraddress4="https://iot.wuliancloud.com/"

        for i in (serveraddress1,serveraddress2,serveraddress3,serveraddress4):
            serverAddress.append(i)
        return serverAddress