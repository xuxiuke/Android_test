import unittest

from test_interfacecase.common import msg
from test_interfacecase.common.process.ssoProcess import ssoProcess


class ssoTest(unittest.TestCase):
    def setUp(self):
        self.response=ssoProcess()

    def tearDown(self):
        self.response=None


    #1、post接口，手机号登陆
    def testLoginByPhone(self):
        self.assertEqual(self.response.loginByPhone(),"0",msg=msg.phoneFailed)

    #2、get接口，token换取mqtt连接信息
    def testTokenMqtt(self):
        self.assertEqual(self.response.tokenMqtt(),"0",msg=msg.mqttFailed)

    #3、	三方账号登录时绑定手机或邮箱，如果该手机或邮箱已绑定了同类型的三方账号，用户确认替换之前的账号时调用此接口；
    def testLoginThirdUpdate(self):
        self.assertEqual(self.response.loginThirdUpdate(),"0",msg=msg.loginThirdUpdate)

    #4、三方账号登录时绑定的手机或邮箱没有注册过账号，利用该手机或邮箱注册新的账号,只能注册一次
    # def testRegBythird(self):
    #     self.assertEqual(self.response.regBythird(),"0",msg=msg.regBythird)

    # 5、三方账号登录时绑定手机或邮箱,
    # 验证码错误gg
    def testLoginThirdbind(self):
        self.assertEqual(self.response.loginThirdbind(), "0", msg=msg.loginThirdbind)

    # 6、通过手机号注册用户
    # 验证码错误gg
    def testRegByphone(self):
        self.assertEqual(self.response.regByphone(), "0", msg=msg.regByphone)

    # 7、通过手机号或者邮箱找回密码并登陆
    # 验证码错误gg
    def testUpdatePassAndLogin(self):
        self.assertEqual(self.response.updatePassAndLogin(), "0", msg=msg.updatePassAndLogin)

  #8、通过手机号或者邮箱注册用户并登陆
    def testRegistByEmailAndPhone(self):
        self.assertEqual(self.response.registByEmailAndPhone(), "0", msg=msg.registByEmailAndPhone)

 # 9、第三方账号注册、登录
    def testLoginBythird(self):
        self.assertEqual(self.response.loginBythird(), "0", msg=msg.loginBythird)

  # 10、邮箱+密码登录
    def testLoginByemail(self):
        self.assertEqual(self.response.loginByemail(), "0", msg=msg.loginByemail)

  # 11、通过校验验证码完成用户的登录
    def testLoginPhoneEmailLogin(self):
        self.assertEqual(self.response.loginPhoneEmailLogin(), "0", msg=msg.loginPhoneEmailLogin)

    #12、三方账号登录时绑定手机号发送验证码
    def testUserBindthirdPhonecode(self):
        self.assertEqual(self.response.userBindthirdPhonecode(), "0", msg=msg.userBindthirdPhonecode)

    #13、用户找回密码时，发送手机验证码
    def testUserUpdatepassPhonecode(self):
        self.assertEqual(self.response.userUpdatepassPhonecode(), "0", msg=msg.userUpdatepassPhonecode)

    #14、手机注册时发送验证码
    def testRegPhonecode(self):
        self.assertEqual(self.response.regPhonecode(), "0", msg=msg.regPhonecode)

    #15、安卓注册设备
    def testTerminalReg(self):
        self.assertEqual(self.response.terminalReg(), "0", msg=msg.terminalReg)

    #16、ios注册设备
    def testTerminalRegIos(self):
        self.assertEqual(self.response.terminalRegIos(), "0", msg=msg.terminalReg)

    #17、注销账号接口,账号解绑需要重新注册
    def testUserRemoveUser(self):
        self.assertEqual(self.response.userRemoveUser(), "0", msg=msg.userRemoveUser)

    #18、申请邮箱注册
    def testRegByemailcode(self):
        self.assertEqual(self.response.regByemailcode(), "0", msg=msg.regByemailcode)

    #19、退出登录
    def testLoginLogout(self):
        self.assertEqual(self.response.loginLogout(), "0", msg=msg.loginLogout)

    # 20、验证码登录发送验证码
    def testLoginPhoneEmailSendCode(self):
        self.assertEqual(self.response.loginPhoneEmailSendCode(), "0", msg=msg.loginPhoneEmailSendCode)


if __name__ == '__main__':
    unittest.main()
