# coding=utf-8


from test_interfacecase.public.area_city import Area_city
import unittest
from test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Area_cityTestCase(unittest.TestCase):
    def setUp(self):
        self.areacity = Area_city()
        self.loginlogout = Login_logout()

    def test_area_city(self):
        u"""查询城市接口"""
        self.assertEqual(self.areacity.area_city(), "0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.areacity = None


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Area_cityTestCase("test_area_city"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
