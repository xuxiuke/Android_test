# coding=utf-8

"""
作者: Duke
文件名: test_token_mqtt.py
创建时间: 2019/09/12-15:04
"""

import unittest
from case.token_mqtt import Token_mqtt
from public import global_value
from case.login_logout import Login_logout


class Token_mqttTestCase(unittest.TestCase):
    def setUp(self):
        self.tokenmqtt = Token_mqtt()
        self.loginlogout = Login_logout()

    def test_token_mqtt(self):
        """"1、SSO接口-token换取mqtt连接信息"""
        global_value.set_execute_value("1")
        self.assertEqual(self.tokenmqtt.token_mqtt(), "0")

    def tearDown(self):
        self.loginlogout.login_logout()
        self.tokenmqtt = None
