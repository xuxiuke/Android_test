# coding=utf-8

import unittest
from test_interfacecase.public.app_updateAppInfo import App_updateAppInfo


class App_updateAppInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.appupdateAppInfo = App_updateAppInfo()

    def test_app_updateAppInfo(self):
        u""""api接口-保存或者更新app信息接口"""
        self.assertEqual(self.appupdateAppInfo.app_updateAppInfo(), "0")

    def tearDown(self):
        self.appupdateAppInfo = None


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(App_updateAppInfoTestCase("test_app_updateAppInfo"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
