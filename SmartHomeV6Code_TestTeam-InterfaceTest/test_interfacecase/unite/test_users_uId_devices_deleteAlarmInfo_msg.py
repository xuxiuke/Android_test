#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_devices_deleteAlarmInfo_msg import Users_uId_devices_deleteAlarmInfo_msg
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_deleteAlarmInfo_msgTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesdeleteAlarmInfomsg = Users_uId_devices_deleteAlarmInfo_msg()
        self.loginlogout = Login_logout()

    def test_users_uId_devices_deleteAlarmInfo_msg(self):
        u""""删除用户消息中心报警日志"""
        self.assertEqual(self.usersuIddevicesdeleteAlarmInfomsg.users_uId_devices_deleteAlarmInfo_msg(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesdeleteAlarmInfomsg = None



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_deleteAlarmInfo_msgTestCase("test_users_uId_devices_deleteAlarmInfo_msg"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)