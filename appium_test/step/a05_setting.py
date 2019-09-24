# coding=utf-8

"""
Created on 2018年9月14日

@author: Duke    设置
"""

from appium_test.PO import base_page
from appium_test.PO import excel
import time


class Setting(base_page.Action):

    # 前置条件：我的页面-》更改手机号页面
    def change_cell_phone_number_page(self):
        self.phone_authentication_page()  # 手机号-身份验证页面
        self.find_id(excel.id_con('et_verification')).send_keys('123456')  # 输入验证码
        self.find_id(excel.id_con('tv_confirm')).click()  # 点击验证成功后即可换绑手机号按钮
        time.sleep(1)

    # 前置条件：我的页面-》修改密码页面
    def change_password_page(self):
        self.password_authentication_page()  # 修改密码-身份验证页面
        self.find_id(excel.id_con('et_verification')).send_keys('123456')  # 输入验证码
        self.find_id(excel.id_con('tv_confirm')).click()  # 点击验证成功后即可修改密码按钮
        self.wait_ac(excel.activity_con('change_password_activity'))  # 确保进入修改密码页面
        time.sleep(1)

    # 前置条件：我的页面-》修改密码-身份验证页面
    def password_authentication_page(self):
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_security')).click()  # 点击账号安全
        time.sleep(1)
        self.find_id(excel.id_con('item_account_security_account_info')).click()  # 点击修改密码
        time.sleep(1)

    # 前置条件：我的页面-》手机号-身份验证页面
    def phone_authentication_page(self):
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_security')).click()  # 点击账号安全
        time.sleep(1)
        self.find_id(excel.id_con('item_account_security_phone')).click()  # 点击手机号
        time.sleep(1)

    # 前置条件：我的页面-》邮箱-身份验证页面
    def mail_authentication_page(self):
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_security')).click()  # 点击账号安全
        time.sleep(1)
        self.find_id(excel.id_con('item_account_security_mail')).click()  # 点击邮箱
        time.sleep(2)

    # 前置条件，我的页面-》报警语音页面
    def alarm_voice_page(self):
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_alarm_voice')).click()  # 点击报警语音
        self.wait_ac(excel.activity_con('alarm_voice_activity'))  # 确保进入报警语音页面
        time.sleep(1)

    # 1、设置-账号安全，身份验证，不填验证码，验证成功后即可换绑手机号按钮不可点击
    def authentication_button(self):
        self.account_login()  # 账号登陆
        self.phone_authentication_page()  # 手机号-身份验证页面
        return self.find_id(excel.id_con('tv_confirm')).is_enabled()  # 验证验证成功后即可换绑手机号按钮是否可点击

    # 2、设置-账号按钮，身份验证，错误验证码，toast提示：验证码错误
    def authentication_wrong_code(self):
        self.account_login()  # 账号登陆
        self.phone_authentication_page()  # 手机号-身份验证页面
        self.find_id(excel.id_con('et_verification')).send_keys('565656')  # 输入错误验证码
        self.find_id(excel.id_con('tv_confirm')).click()  # 点击验证成功后即可换绑手机号按钮
        return self.find_toast('验证码错误')

    # 3、设置-账号按钮，身份验证，小于6位验证码，toast提示：验证码错误
    def authentication_code_6(self):
        self.account_login()  # 账号登陆
        self.phone_authentication_page()  # 手机号-身份验证页面
        self.find_id(excel.id_con('et_verification')).send_keys('12345')  # 输入5位验证码
        self.find_id(excel.id_con('tv_confirm')).click()  # 点击验证成功后即可换绑手机号按钮
        return self.find_toast('验证码错误')

    # 4、设置-账号按钮，更改手机号，不输入手机号，直接点击获取验证码按钮，toast提示：手机号不能为空
    def phonepage_no_phone(self):
        self.account_login()  # 账号登陆
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_id(excel.id_con('tv_get_verification')).click()  # 点击获取验证码
        return self.find_toast('手机号不能为空')

    # 5、设置-账号按钮，更改手机号，输入手机号，不输入验证码，更改手机号按钮不可点击
    def phonepage_button_no_code(self):
        self.account_login()  # 账号登陆
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_id(excel.id_con('et_register_phone_number')).send_keys('18013986382')  # 输入手机号
        return self.find_id(excel.id_con('tv_register_button')).is_enabled()  # 验证更改手机号按钮是否可点击

    # 6、设置-账号按钮，更改手机号，输入验证码，不输入手机号，更改手机号按钮不可点击
    def phonepage_button_no_phone(self):
        self.account_login()  # 账号登陆
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_id(excel.id_con('et_verification')).send_keys('123456')  # 输入验证码
        return self.find_id(excel.id_con('tv_register_button')).is_enabled()  # 验证更改手机号按钮是否可点击

    # 7、设置-账号按钮，更改手机号，输入错误手机号，输入验证码，点击更改手机号按钮，toast提示：手机号格式错误
    def phonepage_wrong_phone(self):
        self.account_login()  # 账号登陆
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_id(excel.id_con('et_register_phone_number')).send_keys('1801398')  # 输入错误手机号
        self.find_id(excel.id_con('et_verification')).send_keys('123456')  # 输入验证码
        self.find_id(excel.id_con('tv_register_button')).click()  # 点击更改手机号按钮
        return self.find_toast('手机号格式错误')

    # 8、设置-账号按钮，更改手机号，输入手机号，输入错误验证码，点击更改手机号按钮，toast提示：验证码错误
    def phonepage_wrong_code(self):
        self.account_login()  # 账号登陆
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_id(excel.id_con('et_register_phone_number')).send_keys('18013986382')  # 输入手机号
        self.find_id(excel.id_con('et_verification')).send_keys('455612')  # 输入错误验证码
        self.find_id(excel.id_con('tv_register_button')).click()  # 点击更改手机号按钮
        return self.find_toast('验证码错误')

    # 9、设置-账号按钮，更改手机号，输入手机号，输入小于6位验证码，点击更改手机号按钮，toast提示：验证码错误
    def phonepage_code_6(self):
        self.account_login()  # 账号登陆
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_id(excel.id_con('et_register_phone_number')).send_keys('18013986382')  # 输入手机号
        self.find_id(excel.id_con('et_verification')).send_keys('12345')  # 输入验证码少于6位
        self.find_id(excel.id_con('tv_register_button')).click()  # 点击更改手机号按钮
        return self.find_toast('验证码错误')

    # 10、设置-账号按钮，更改手机号，输入已注册手机号，输入验证码，点击更改手机号按钮，toast提示：用户已存在
    def phonepage_old_user(self):
        self.account_login()  # 账号登陆
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_id(excel.id_con('et_register_phone_number')).send_keys('18013986382')  # 输入手机号
        self.find_id(excel.id_con('et_verification')).send_keys('123456')  # 输入验证码少于6位
        self.find_id(excel.id_con('tv_register_button')).click()  # 点击更改手机号按钮
        return self.find_toast('用户已存在')

    # 11、设置-账号安全-邮箱，不输入验证码，验证成功后即可换绑邮箱（邮箱验证码没有设置为123456，大部分用例不可翻译，省略，同更改手机号）按钮，不可点击
    def mail_no_code(self):
        self.account_login()  # 账号登陆
        self.mail_authentication_page()  # 我的页面-邮箱-身份验证页面
        return self.find_id(excel.id_con('tv_confirm')).is_enabled()  # 验证验证成功后即可换绑邮箱按钮是否可点击

    # 12、设置-账号安全-邮箱，输入错误验证码，toast提示：验证码失效
    def mail_wrong_code(self):
        self.account_login()  # 账号登陆
        self.mail_authentication_page()  # 我的页面-邮箱-身份验证页面
        self.find_id(excel.id_con('et_verification')).send_keys('524163')  # 输入错误验证码
        self.find_id(excel.id_con('tv_confirm')).click()  # 点击验证成功后即可换绑邮箱按钮
        return self.find_toast('验证码失效')

    # 13、设置-账号安全-修改密码，不输入验证码，验证成功后即可修改密码按钮，不可点击
    def password_no_code(self):
        self.account_login()  # 账号登陆
        self.password_authentication_page()  # 修改密码-身份验证页面
        return self.find_id(excel.id_con('tv_confirm')).is_enabled()  # 验证验证成功后即可修改密码按钮是否可点击

    # 14、设置-账号安全-修改密码，输入错误密码，点击验证成功后即可修改密码按钮，toast提示：验证码错误
    def password_wrong_code(self):
        self.account_login()  # 账号登陆
        self.password_authentication_page()  # 修改密码-身份验证页面
        self.find_id(excel.id_con('et_verification')).send_keys('635241')  # 输入错误的验证码
        self.find_id(excel.id_con('tv_confirm')).click()  # 点击验证成功后即可修改密码按钮
        return self.find_toast('验证码错误')

    # 15、设置-账号安全-修改密码-修改密码，不输入新密码，确定按钮不可点击
    def password_no_new_password(self):
        self.account_login()  # 账号登陆
        self.change_password_page()  # 修改密码页面
        return self.find_id(excel.id_con('confirm_pwd_button')).is_enabled()  # 验证确定按钮是否可点击

    # 16、设置-账号安全-修改密码-修改密码，输入少于6位新密码，toast提示：密码长度不能小于6个字符
    def password_new_password_6(self):
        self.account_login()  # 账号登陆
        self.change_password_page()  # 修改密码页面
        self.find_id(excel.id_con('new_pwd_editText')).send_keys('m12345')  # 输入少于6位新密码
        self.find_id(excel.id_con('confirm_pwd_button')).click()  # 点击确定按钮
        return self.find_toast('密码长度不能小于8个字符')

    # 17、设置-账号安全-修改密码-修改密码，输入全数字新密码，toast提示：密码至少有数字、字母或符号的2种组合
    def password_new_number_password(self):
        self.account_login()  # 账号登陆
        self.change_password_page()  # 修改密码页面
        self.find_id(excel.id_con('new_pwd_editText')).send_keys('1234567890')  # 输入全数字新密码
        self.find_id(excel.id_con('confirm_pwd_button')).click()  # 点击确定按钮
        return self.find_toast('密码至少有数字、字母或符号的2种组合')

    # 18、设置-账号安全-修改密码-修改密码，输入全字母新密码，toast提示：密码至少有数字、字母或符号的2种组合
    def password_new_letter_password(self):
        self.account_login()  # 账号登陆
        self.change_password_page()  # 修改密码页面
        self.find_id(excel.id_con('new_pwd_editText')).send_keys('qazxswedc')  # 输入全字母新密码
        self.find_id(excel.id_con('confirm_pwd_button')).click()  # 点击确定按钮
        return self.find_toast('密码至少有数字、字母或符号的2种组合')

    # 19、设置-账号安全-修改密码-修改密码，输入正确的新密码，返回我的页面
    def new_password(self):
        self.account_login()  # 账号登陆
        self.change_password_page()  # 修改密码页面
        self.find_id(excel.id_con('new_pwd_editText')).send_keys('wl123456789')  # 输入新密码
        self.find_id(excel.id_con('confirm_pwd_button')).click()  # 点击确定按钮
        return self.wait_ac(excel.activity_con('home_activity'))  # 我的页面

    # 20、设置-推送通知，关闭按钮，设备推送管理等隐藏
    def close_push(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_alarm_user')).click()  # 点击关闭推送通知
        return self.find_item('设备推送管理')

    # 21、设置-推送通知，打开按钮，推送时间等展开
    def open_push(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_alarm_user')).click()  # 点击关闭推送通知
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_alarm_user')).click()  # 再点击打开
        return self.find_item('推送时间')

    # 22、设置-报警语音-报警语音，关闭按钮，语速等隐藏
    def closing_alarm_speech(self):
        self.account_login()  # 账号登陆
        self.alarm_voice_page()  # 报警语音页面
        self.find_id(excel.id_con('item_remind_alarm_voice')).click()  # 点击报警语音开关按钮，关闭
        return self.find_item('语速')

    # 23、设置-报警语音-报警语音，打开按钮，语种等展开
    def open_alarm_speech(self):
        self.account_login()  # 账号登陆
        self.alarm_voice_page()  # 报警语音页面
        self.find_id(excel.id_con('item_remind_alarm_voice')).click()  # 点击报警语音开关按钮，关闭
        time.sleep(1)
        self.find_id(excel.id_con('item_remind_alarm_voice')).click()  # 点击报警语音开关按钮，打开
        return self.find_item('语种')

    # 24、设置，点击推送时间
    def push_time(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_push_time')).click()  # 点击推送时间
        time.sleep(1)
        return self.find_item('00')

    # 25、设置，点击设置推送管理
    def push_manage(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_push_manage')).click()  # 点击设置推送管理
        time.sleep(2)
        return self.find_item('管家任务执行通知')

    # 26、设置，点击换肤中心
    def setting_skin(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_skin')).click()  # 点击换肤中心
        time.sleep(2)
        return self.find_id(excel.id_con('iv_preview'))  # 验证可以找到皮肤元素

    # 27、设置，点击清理缓存
    def setting_cache(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_cache')).click()  # 点击清理缓存
        return self.find_toast('清理缓存')

    # 28、设置，点击退出登陆
    def drop_out(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_setting')).click()  # 点击设置
        time.sleep(1)
        self.find_id(excel.id_con('item_setting_logout')).click()  # 点击退出登陆
        return self.find_toast('退出登录成功')
