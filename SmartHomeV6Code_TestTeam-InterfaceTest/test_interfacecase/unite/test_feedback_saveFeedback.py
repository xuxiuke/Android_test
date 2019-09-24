#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.feedback_saveFeedback import Feedback_saveFeedback
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Feedback_saveFeedbackTestCase(unittest.TestCase):
    def setUp(self):
        self.feedbacksaveFeedback = Feedback_saveFeedback()
        self.loginlogout = Login_logout()

    def test_feedback_saveFeedback(self):
        u""""保存用户意见反馈"""
        self.assertEqual(self.feedbacksaveFeedback.feedback_saveFeedback(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.feedbacksaveFeedback = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Feedback_saveFeedbackTestCase("test_feedback_saveFeedback"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)