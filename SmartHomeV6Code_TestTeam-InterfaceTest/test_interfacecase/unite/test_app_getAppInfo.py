# coding=utf-8

import unittest
from test_interfacecase.public.app_getAppinfo import App_getAppInfo
from test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class App_getAppInfoTestCase(unittest.TestCase):

    def setUp(self):
        self.appgetAppinfo = App_getAppInfo()
        self.loginlogout = Login_logout()

    def test_app_getAppinfo(self):
        """"api接口-APP检查更新的接口"""
        self.assertEqual(self.appgetAppinfo.app_getAppInfo(), "0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.appgetAppinfo = None


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(App_getAppInfoTestCase("test_app_getAppinfo"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
