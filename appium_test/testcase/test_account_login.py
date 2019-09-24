# coding=utf-8

"""
Created on 2018年9月6日

@author: Duke    账号登陆+物联会员+意见反馈+关于+个人信息+网关中心    42条用例
"""

from PO.open_app import Open_app
from step import a04_account_login
import unittest
import time
from PO import excel


# @unittest.skip(u'添加场景、区域，跳过测试')
class Test004(unittest.TestCase, a04_account_login.Account_login):  # TestCase类，所有测试用例类继承的基本类
    """账号登陆+物联会员+意见反馈+关于+个人信息+网关中心测试"""

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

    # 1、账号登陆，未绑定网关-首页
    def test_home_page(self):
        self.assertTrue(self.home_page(), '账号登陆首页失败')

    # 2、账号登陆，未绑定网关-查看小铃铛报警消息
    def test_alarm_message(self):
        self.assertTrue(self.alarm_message())

    # 3、账号登陆，未绑定网关-查看小铃铛日志消息
    def test_log_message(self):
        self.assertTrue(self.log_message())

    # 4、账号登陆，未绑定网关-点击场景，弹出尚未绑定网关编辑框
    def test_click_the_scene(self):
        self.assertTrue(self.click_the_scene())

    # 5、账号登陆，未绑定网关-尚未登录绑定网关编辑框，点击取消按钮，编辑框消失
    def test_unlogged_gateway_editbox_cancel(self):
        self.assertFalse(self.unlogged_gateway_editbox_cancel())

    # 6、账号登陆，未绑定网关-点击场景，点击去绑定，进入网关列表页面
    def test_clicK_the_scene_binding(self):
        self.assertTrue(self.click_the_scene_binding())

    # 7、账号登陆，未绑定网关-点击场景，点击体验网关试用按钮，toast提示：体验网关会在10分钟后自动解绑
    def test_click_trial_gateway(self):
        self.assertTrue(self.click_trial_gateway())

    # 8、账号登陆，未绑定网关-点击设备，暂无设备
    def test_click_the_devide(self):
        self.assertTrue(self.click_the_device())

    # 9、账号登陆，未绑定网关-点击发现，Wulian商场
    def test_click_the_find(self):
        self.assertTrue(self.clicK_the_find())

    # 10、账号登陆，未绑定网关-绑定网关流程
    def test_bound_gateway(self):
        self.assertNotEqual(self.bound_gateway(), '未登录网关', '网关绑定失败')

    # 11、账号登陆，未绑定网关-绑定网关流程,不输入账号
    def test_bound_gateway_no_id(self):
        self.assertFalse(self.bound_gateway_no_id())

    # 12、账号登陆，未绑定网关-绑定网关流程,不输入密码
    def test_bound_gateway_no_password(self):
        self.assertFalse(self.bound_gateway_no_password())

    # 13、账号登陆，未绑定网关-绑定网关流程,输入密码少于6位
    def test_bound_gateway_password5(self):
        self.assertFalse(self.bound_gateway_password5())

    # 14、账号登陆，未绑定网关-绑定网关流程,输入错误密码
    def test_bound_gateway_wrong_password(self):
        self.assertTrue(self.bound_gateway_wrong_password())

    # 15、我的页面，进入物联会员
    def test_wulian_member(self):
        self.assertTrue(self.wulian_member())

    # 16、我的页面，物联会员，进入积分变动记录页面
    def test_integral_change(self):
        self.assertTrue(self.integral_change())

    # 17、我的页面，物联会员，签到规则
    def test_sign_in_rules(self):
        self.assertTrue(self.sign_in_rules())

    # 18、我的页面，物联会员，会员说明
    def test_member_description(self):
        self.assertTrue(self.member_description())

    # 19、我的页面，物联会员，积分说明
    def test_integral_explanation(self):
        self.assertTrue(self.integral_explanantion())

    # 20、我的页面，进入意见反馈页面
    def test_feed_back(self):
        self.assertTrue(self.feed_back())

    # 21、意见反馈，不输入内容，提交按钮不可点击
    def test_feed_back_submit(self):
        self.assertFalse(self.feed_back_submit())

    # 22、意见反馈，提交意见
    def test_feed_back_edit(self):
        self.assertTrue(self.feed_back_edit())

    # 23、关于-功能介绍
    def test_about_introduction(self):
        self.assertTrue(self.about_introduction())

    # 24、关于-关于物联
    def test_about_wulian(self):
        self.assertTrue(self.about_wulian())

    # 25、个人信息-点击头像
    def test_head_portrait(self):
        self.assertTrue(self.head_portrait())

    # 26、个人信息-点击头像,点击取消，编辑框消失
    def test_head_portrait_cancel(self):
        self.assertFalse(self.head_portrait_cancel())

    # 27、个人信息-修改名称
    def test_modify_the_name(self):
        self.assertTrue(self.modify_the_name())
        # 改回名称
        time.sleep(1)
        self.find_id(excel.id_con('setting_manager_item_name')).click()  # 点击名称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'Duke正式服')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮

    # 28、个人信息-修改名称，取消
    def test_modify_the_name_cancel(self):
        self.assertFalse(self.modify_the_name_cancel())

    # 29、个人信息-修改名称，不输入点击确定，点击无效，修改名称弹窗还在
    def test_modify_the_name_determine(self):
        self.assertTrue(self.modify_the_name_determine())

    # 30、网关中心-已绑定网关
    def test_bound_gateway_list(self):
        self.assertTrue(self.bound_gateway_list())

    # 31、网关中心-已接受分享
    def test_acceptance_of_sharing(self):
        self.assertTrue(self.acceptance_of_sharing())

    # 32、网关设置-修改网关昵称
    def test_gateway_name(self):
        self.assertTrue(self.gateway_name())
        # 改回昵称
        self.find_id(excel.id_con('item_gateway_center_setting')).click()  # 点击网关设置
        time.sleep(1)
        self.find_id(excel.id_con('item_gateway_setting_name')).click()  # 点击网关昵称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'呵呵')  # 输入网关新昵称
        time.sleep(2)
        self.find_id(excel.id_con('dialog_btn_positive')).click()

    # 33、网关设置-修改网关昵称，取消
    def test_gateway_name_cancel(self):
        self.assertFalse(self.gateway_name_cancel())

    # 34、网关设置-修改网关昵称，不输入点击确定
    def test_gateway_no_name(self):
        self.assertTrue(self.gateway_no_name())

    # 35、网关设置-修改密码
    def test_change_password(self):
        self.assertTrue(self.change_password())
        # 改回密码
        self.find_id(excel.id_con('item_gateway_center')).click()  # 点击网关中心
        time.sleep(2)
        self.modify_gateway_password('wl123456789', 'qazwsx1234')

    # 36、网关设置-修改密码-未填写原始密码
    def test_change_no_old_password(self):
        self.assertFalse(self.change_no_old_password())

    # 37、网关设置-修改密码-未填写新密码
    def test_change_no_new_password(self):
        self.assertFalse(self.change_no_new_password())

    # 38、网关设置-修改密码-错错的原始密码，toast提示：修改失败
    def test_change_wrong_old_password(self):
        self.assertTrue(self.change_wrong_old_password())

    # 39、网关设置-修改密码-新密码全数字，toast提示：密码至少有数字、字母或符号的2种组合
    def test_change_number_password(self):
        self.assertTrue(self.change_number_password())

    # 40、网关设置-修改密码-新密码全字母，toast提示：密码至少有数字、字母或符号的2种组合
    def test_change_letter_password(self):
        self.assertTrue(self.change_letter_password())

    # 41、网关设置-修改密码-新密码小于6位，toast提示：密码长度不能小于6个字符
    def test_change_password_6(self):
        self.assertTrue(self.change_password_6())

    # 42、网关设置-修改密码-新密码与原始密码相同，toast提示：新密码不能和老密码相同
    def test_change_same_password(self):
        self.assertTrue(self.change_same_password())
