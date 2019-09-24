#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from  test_interfacecase.public.token_mqtt import Token_mqtt
from test_interfacecase.bussiness import global_value
from  test_interfacecase.public.login_logout import Login_logout


class Token_mqttTestCase(unittest.TestCase):
    def setUp(self):
        self.tokenmqtt = Token_mqtt()
        self.loginlogout = Login_logout()


    def test_token_mqtt(self):
        u""""token换取mqtt连接信息"""
        global_value.set_execute_value("1")
        self.assertEqual(self.tokenmqtt.token_mqtt(),"0")

    def tearDown(self):
        self.loginlogout.login_logout()
        self.tokenmqtt= None




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Token_mqttTestCase("test_token_mqtt"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
