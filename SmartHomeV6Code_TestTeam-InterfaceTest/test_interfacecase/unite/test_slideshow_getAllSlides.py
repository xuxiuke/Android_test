#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.slideshow_getAllSlides import Slideshow_getAllSlides
from  test_interfacecase.bussiness.kernal_function import Kernal_function
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Slideshow_getAllSlidesTestCase(unittest.TestCase):
    def setUp(self):
        self.slideshowgetAllSlides = Slideshow_getAllSlides()
        self.loginlogout = Login_logout()


    def test_slideshow_getAllSlides(self):
        u""""获取banner列表"""
        self.assertEqual(self.slideshowgetAllSlides.slideshow_getAllSlides(),"0")


    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.slideshowgetAllSlides = None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Slideshow_getAllSlidesTestCase("test_slideshow_getAllSlides"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)