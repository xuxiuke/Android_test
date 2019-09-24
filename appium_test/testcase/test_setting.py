# coding=utf-8

"""
Created on 2018年9月14日

@author: Duke    设置    28条用例
"""

from PO.open_app import Open_app
from step import a05_setting
import unittest
import time
from PO import excel


# @unittest.skip(u'添加场景、区域，跳过测试')
class Test005(unittest.TestCase, a05_setting.Setting):  # TestCase类，所有测试用例类继承的基本类
    """设置测试"""

    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        self.ina = Open_app(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 1、设置-账号安全，身份验证，不填验证码，验证成功后即可换绑手机号按钮不可点击
    def test_authentication_button(self):
        self.assertFalse(self.authentication_button())

    # 2、设置-账号按钮，身份验证，错误验证码，toast提示：验证码错误
    def test_authentication_wrong_code(self):
        self.assertTrue(self.authentication_wrong_code())

    # 3、设置-账号按钮，身份验证，小于6位验证码，toast提示：验证码错误
    def test_authentication_code_6(self):
        self.assertTrue(self.authentication_code_6())

    # 4、设置-账号按钮，更改手机号，不输入手机号，直接点击获取验证码按钮，toast提示：手机号不能为空
    def test_phonepage_no_phone(self):
        self.assertTrue(self.phonepage_no_phone())

    # 5、设置-账号按钮，更改手机号，输入手机号，不输入验证码，更改手机号按钮不可点击
    def test_phonepage_button_no_code(self):
        self.assertFalse(self.phonepage_button_no_code())

    # 6、设置-账号按钮，更改手机号，输入验证码，不输入手机号，更改手机号按钮不可点击
    def test_phonepage_button_no_phone(self):
        self.assertFalse(self.phonepage_button_no_phone())

    # 7、设置-账号按钮，更改手机号，输入错误手机号，输入验证码，点击更改手机号按钮，toast提示：手机号格式错误
    def test_phonepage_wrong_phone(self):
        self.assertTrue(self.phonepage_wrong_phone())

    # 8、设置-账号按钮，更改手机号，输入手机号，输入错误验证码，点击更改手机号按钮，toast提示：验证码错误
    def test_phonepage_wrong_code(self):
        self.assertTrue(self.phonepage_wrong_code())

    # 9、设置-账号按钮，更改手机号，输入手机号，输入小于6位验证码，点击更改手机号按钮，toast提示：验证码错误
    def test_phonepage_code_6(self):
        self.assertTrue(self.phonepage_code_6())

    # 10、设置-账号按钮，更改手机号，输入已注册手机号，输入验证码，点击更改手机号按钮，toast提示：用户已存在
    def test_phonepage_old_user(self):
        self.assertTrue(self.phonepage_old_user())

    # 11、设置-账号安全-邮箱，不输入验证码，验证成功后即可换绑邮箱（邮箱验证码没有设置为123456，大部分用例不可翻译，省略，同更改手机号）按钮，不可点击
    def test_mail_no_code(self):
        self.assertFalse(self.mail_no_code())

    # 12、设置-账号安全-邮箱，输入错误验证码，toast提示：验证码失效
    def test_mail_wrong_code(self):
        self.assertTrue(self.mail_wrong_code())

    # 13、设置-账号安全-修改密码，不输入验证码，验证成功后即可修改密码按钮，不可点击
    def test_password_no_code(self):
        self.assertFalse(self.password_no_code())

    # 14、设置-账号安全-修改密码，输入错误密码，点击验证成功后即可修改密码按钮，toast提示：验证码错误
    def test_password_wrong_code(self):
        self.assertTrue(self.password_wrong_code())

    # 15、设置-账号安全-修改密码-修改密码，不输入新密码，确定按钮不可点击
    def test_password_no_new_password(self):
        self.assertFalse(self.password_no_new_password())

    # 16、设置-账号安全-修改密码-修改密码，输入少于6位新密码，toast提示：密码长度不能小于6个字符
    def test_password_new_password_6(self):
        self.assertTrue(self.password_new_password_6())

    # 17、设置-账号安全-修改密码-修改密码，输入全数字新密码，toast提示：密码至少有数字、字母或符号的2种组合
    def test_password_new_number_password(self):
        self.assertTrue(self.password_new_number_password())

    # 18、设置-账号安全-修改密码-修改密码，输入全字母新密码，toast提示：密码至少有数字、字母或符号的2种组合
    def test_password_new_letter_password(self):
        self.assertTrue(self.password_new_letter_password())

    # 19、设置-账号安全-修改密码-修改密码，输入正确的新密码，返回我的页面
    def test_new_password(self):
        self.assertTrue(self.new_password())

    # 20、设置-推送通知，关闭按钮，设备推送管理等隐藏
    def test_close_push(self):
        self.assertFalse(self.close_push())
        # 打开推送通知
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_alarm_user')).click()

    # 21、设置-推送通知，打开按钮，推送时间等展开
    def test_open_push(self):
        self.assertTrue(self.open_push())

    # 22、设置-报警语音-报警语音，关闭按钮，语速等隐藏
    def test_closing_alarm_speech(self):
        self.assertFalse(self.closing_alarm_speech())
        # 打开报警语音
        time.sleep(1)
        self.find_id(excel.id_con('item_remind_alarm_voice')).click()  # 点击报警语音开关按钮，打开

    # 23、设置-报警语音-报警语音，打开按钮，语种等展开
    def test_open_alarm_speech(self):
        self.assertTrue(self.open_alarm_speech())

    # 24、设置，点击推送时间
    def test_push_time(self):
        self.assertTrue(self.push_time())

    # 25、设置，点击设置推送管理
    def test_push_manage(self):
        self.assertTrue(self.push_manage())

    # 26、设置，点击换肤中心
    def test_setting_skin(self):
        self.assertTrue(self.setting_skin())

    # 27、设置，点击清理缓存
    def test_setting_cache(self):
        self.assertTrue(self.setting_cache())

    # 28、设置，点击退出登陆
    def test_drop_out(self):
        self.assertTrue(self.drop_out())
