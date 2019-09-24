# coding=utf-8

"""
Created on 2018年9月6日

@author: Duke    账号登陆+物联会员+意见反馈+关于+个人信息+网关中心
"""

from appium_test.PO import base_page
from PO import excel
import time


class Account_login(base_page.Action):

    # 1、账号登陆，未绑定网关-首页
    def home_page(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页
        return self.find_item('离家') and self.find_item('睡觉') and self.find_item('起床') and self.find_item(
            '就餐')  # 随机查找4个默认的场景名称

    # 2、账号登陆，未绑定网关-查看小铃铛报警消息
    def alarm_message(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页
        self.find_id(excel.id_con('base_img_right')).click()  # 点击小铃铛
        time.sleep(1)
        self.find_id(excel.id_con('view_back_alarm')).click()  # 点击小铃铛-报警消息
        time.sleep(2)
        return self.find_item('没有报警消息')

    # 3、账号登陆，未绑定网关-查看小铃铛日志消息
    def log_message(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页
        self.find_id(excel.id_con('base_img_right')).click()  # 点击小铃铛
        time.sleep(1)
        self.find_id(excel.id_con('view_back_log')).click()  # 点击小铃铛-日志消息
        time.sleep(2)
        return self.find_item('没有日志消息')

    # 4、账号登陆，未绑定网关-点击场景，弹出尚未登录网关编辑框
    def click_the_scene(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页
        self.find_id(excel.id_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(2)
        return self.find_item('尚未登录网关')

    # 5、账号登陆，未绑定网关-尚未登录绑定网关编辑框，点击取消按钮，编辑框消失
    def unlogged_gateway_editbox_cancel(self):
        self.click_the_scene()  # 未登陆网关情况，尚未登录网关编辑框
        self.find_id('btn_cancel').click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('尚未登录网关')

    # 6、账号登陆，未绑定网关-点击场景，点击去登录，进入网关列表页面
    def click_the_scene_binding(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()
        self.find_id(excel.id_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(1)
        self.find_id(excel.id_con('btn_bind')).click()  # 点击去登录按钮
        return self.wait_ac(excel.activity_con('gateway_list'))  # 验证网关列表页面T或者F

    # 7、账号登陆，未绑定网关-点击场景，点击体验网关试用按钮，toast提示：体验网关会在10分钟后自动解绑
    def click_trial_gateway(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()
        self.find_id(excel.id_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(1)
        self.find_id(excel.id_con('btn_virtual')).click()  # 点击体验网关试用按钮
        return self.find_toast('体验网关会在10分钟后自动解绑')

    # 8、账号登陆，未绑定网关-点击设备，暂无设备
    def click_the_device(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        return self.find_item('暂无设备')

    # 9、账号登陆，未绑定网关-点击智能，弹出尚未登录网关编辑框
    def clicK_the_find(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能
        time.sleep(2)
        return self.find_item('尚未登录网关')

    # 10、账号登陆，未绑定网关-绑定网关流程
    def bound_gateway(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()
        self.find_id(excel.id_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(2)
        self.find_id(excel.id_con('btn_bind')).click()  # 点击去登录按钮
        self.binding_gateway('50294D20B1FC', 'qazwsx1234')  # 登录网关20B1FC
        self.find_id(excel.id_con('img_left')).click()  # 点击返回按钮
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.find_id(excel.id_con('item_gateway_center')).click()  # 点击网关中心
        time.sleep(2)
        text = self.get_text(excel.id_con('item_gateway_center_name'))  # 获取网关中心网关名
        return text

    # 11、账号登陆，未绑定网关-绑定网关流程,不输入账号
    def bound_gateway_no_id(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()
        self.find_id(excel.id_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(1)
        self.find_id(excel.id_con('btn_bind')).click()  # 点击去登录按钮
        self.find_id(excel.id_con('img_right')).click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('et_gateway_username')).send_keys('')  # 输入网关ID
        self.find_id(excel.id_con('et_gateway_password')).send_keys('qazwsx1234')  # 输入网关密码
        return self.find_id(excel.id_con('btn_gateway_login')).is_enabled()  # 验证按钮是否可点击

    # 12、账号登陆，未绑定网关-绑定网关流程,不输入密码
    def bound_gateway_no_password(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()
        self.find_id(excel.id_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(1)
        self.find_id(excel.id_con('btn_bind')).click()  # 点击去登录按钮
        self.find_id(excel.id_con('img_right')).click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('et_gateway_username')).send_keys('50294D20B1FC')  # 输入网关ID
        self.find_id(excel.id_con('et_gateway_password')).send_keys('')  # 输入网关密码
        return self.find_id(excel.id_con('btn_gateway_login')).is_enabled()  # 验证按钮是否可点击

    # 13、账号登陆，未绑定网关-绑定网关流程,输入密码少于6位
    def bound_gateway_password5(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()
        self.find_id(excel.id_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(1)
        self.find_id(excel.id_con('btn_bind')).click()  # 点击去登录按钮
        self.find_id(excel.id_con('img_right')).click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('et_gateway_username')).send_keys('50294D20B1FC')  # 输入网关ID
        self.find_id(excel.id_con('et_gateway_password')).send_keys('wl123')  # 输入网关密码
        return self.find_id(excel.id_con('btn_gateway_login')).is_enabled()  # 验证按钮是否可点击

    # 14、账号登陆，未绑定网关-绑定网关流程,输入错误密码
    def bound_gateway_wrong_password(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()
        self.find_id(excel.id_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(1)
        self.find_id(excel.id_con('btn_bind')).click()  # 点击去登录按钮
        self.find_id(excel.id_con('img_right')).click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('et_gateway_username')).send_keys('50294D20B1FC')  # 输入网关ID
        self.find_id(excel.id_con('et_gateway_password')).send_keys('wl123456')  # 输入网关密码
        self.find_id(excel.id_con('btn_gateway_login')).click()  # 点击绑定网关按钮
        return self.find_toast('设备密码错误')

    # 15、我的页面，进入物联会员
    def wulian_member(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_member_center')).click()  # 点击物联会员
        time.sleep(5)
        return self.wait_ac(excel.activity_con('member_center'))  # 验证会员页面F或者T

    # 16、我的页面，物联会员，进入积分变动记录页面
    def integral_change(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_member_center')).click()  # 点击物联会员
        time.sleep(5)
        self.wait_ac(excel.activity_con('member_center'))
        self.find_xpath(excel.xpath_con('integral_tips')).click()  # 点击积分变动记录
        time.sleep(5)
        return self.find_item('使用一次场景')

    # 17、我的页面，物联会员，签到规则
    def sign_in_rules(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_member_center')).click()  # 点击物联会员
        time.sleep(5)
        self.wait_ac(excel.activity_con('member_center'))
        self.find_xpath(excel.xpath_con('sign_in_rules')).click()  # 点击签到规则
        time.sleep(1)
        return self.find_item('签到规则')

    # 18、我的页面，物联会员，会员说明
    def member_description(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_member_center')).click()  # 点击物联会员
        time.sleep(5)
        self.wait_ac(excel.activity_con('member_center'))
        self.find_xpath(excel.xpath_con('member_description')).click()  # 点击XX会员
        time.sleep(1)
        return self.find_item('会员说明')

    # 19、我的页面，物联会员，积分说明
    def integral_explanantion(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_member_center')).click()  # 点击物联会员
        time.sleep(5)
        self.wait_ac(excel.activity_con('member_center'))
        self.find_xpath(excel.xpath_con('integral_explanation')).click()  # 点击积分说明
        time.sleep(1)
        return self.find_item('积分说明')

    # 20、我的页面，进入意见反馈页面
    def feed_back(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_customer_feedback')).click()  # 点击意见反馈
        return self.wait_ac(excel.activity_con('feed_back'))

    # 21、意见反馈，不输入内容，提交按钮不可点击
    def feed_back_submit(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_customer_feedback')).click()  # 点击意见反馈
        self.wait_ac(excel.activity_con('feed_back'))
        return self.find_id(excel.id_con('feedback_button_submit')).is_enabled()  # 验证提交按钮禁用

    # 22、意见反馈，提交意见
    def feed_back_edit(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_customer_feedback')).click()  # 点击意见反馈
        self.wait_ac(excel.activity_con('feed_back'))
        self.find_id(excel.id_con('feedback_edit_msg')).send_keys(u'Android自动化测试')  # 输入
        self.find_id(excel.id_con('feedback_button_submit')).click()  # 点击提交按钮
        return self.find_toast('提交成功')

    # 23、关于-功能介绍
    def about_introduction(self):
        self.account_login()  # 账号登陆
        self.swipeUp(1000)  # 上划一次
        self.find_id(excel.id_con('item_about')).click()  # 点击关于
        time.sleep(1)
        self.find_id(excel.id_con('item_about_us_introduction')).click()  # 点击功能介绍
        return self.wait_ac(excel.activity_con('introduction'))

    # 24、关于-关于物联
    def about_wulian(self):
        self.account_login()  # 账号登陆
        self.swipeUp(1000)  # 上划一次
        self.find_id(excel.id_con('item_about')).click()  # 点击关于
        time.sleep(1)
        self.find_id(excel.id_con('item_about_us_about')).click()  # 点击功能介绍
        time.sleep(1)
        return self.find_item('南京物联传感技术有限公司')

    # 25、个人信息-点击头像
    def head_portrait(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_account_login')).click()  # 点击个人信息
        time.sleep(1)
        self.find_id(excel.id_con('setting_manager_item_name_ly')).click()  # 点击头像，弹出编辑框
        time.sleep(1)
        return self.find_item('拍照')

    # 26、个人信息-点击头像,点击取消，编辑框消失
    def head_portrait_cancel(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_account_login')).click()  # 点击个人信息
        time.sleep(1)
        self.find_id(excel.id_con('setting_manager_item_name_ly')).click()  # 点击头像，弹出编辑框
        self.find_id(excel.id_con('popup_choose_portrait_cancel')).click()  # 点击取消按钮
        return self.find_item('拍照')

    # 27、个人信息-修改名称
    def modify_the_name(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_account_login')).click()  # 点击个人信息
        time.sleep(1)
        self.find_id(excel.id_con('setting_manager_item_name')).click()  # 点击名称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'自动化测试-修改昵称')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_item('自动化测试-修改昵称')

    # 28、个人信息-修改名称，取消
    def modify_the_name_cancel(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_account_login')).click()  # 点击个人信息
        time.sleep(1)
        self.find_id(excel.id_con('setting_manager_item_name')).click()  # 点击名称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'自动化测试-修改昵称222')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        return self.find_item('自动化测试-修改昵称222')

    # 29、个人信息-修改名称，不输入点击确定，点击无效，修改名称弹窗还在
    def modify_the_name_determine(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_account_login')).click()  # 点击个人信息
        time.sleep(1)
        self.find_id(excel.id_con('setting_manager_item_name')).click()  # 点击名称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys('')  # 不输入
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_item('修改名字')  # 验证修改名称弹窗还在

    # 30、网关中心-已绑定网关
    def bound_gateway_list(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        text = self.get_text(excel.id_con('item_gateway_center_name'))  # 获取网关中心网关名
        self.find_id(excel.id_con('item_gateway_center_list')).click()  # 点击网关列表
        time.sleep(2)
        return self.find_item(text)

    # 31、网关中心-已接受分享
    def acceptance_of_sharing(self):
        self.account_login()  # 账号登陆
        self.find_id(excel.id_con('item_gateway_center')).click()  # 点击网关中心
        time.sleep(1)
        self.find_id(excel.id_con('item_gateway_center_list')).click()  # 点击网关列表
        time.sleep(2)
        self.find_id(excel.id_con('rb_tab_auth_gateway')).click()  # 点击已接受分享
        return self.find_item('暂无他人分享')

    # 32、网关设置-修改网关昵称
    def gateway_name(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_id(excel.id_con('item_gateway_center_setting')).click()  # 点击网关设置
        time.sleep(2)
        self.find_id(excel.id_con('item_gateway_setting_name')).click()  # 点击网关昵称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'自动化测试-网关昵称')  # 输入网关新昵称
        time.sleep(2)
        self.find_id(excel.id_con('dialog_btn_positive')).click()
        time.sleep(2)
        self.driver.back()  # 返回上一页
        return self.find_item('自动化测试-网关昵称')

    # 33、网关设置-修改网关昵称，取消
    def gateway_name_cancel(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_id(excel.id_con('item_gateway_center_setting')).click()  # 点击网关设置
        time.sleep(2)
        self.find_id(excel.id_con('item_gateway_setting_name')).click()  # 点击网关昵称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'哈哈111')  # 输入网关新昵称
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(2)
        self.driver.back()  # 返回上一页
        return self.find_item('哈哈111')

    # 34、网关设置-修改网关昵称，不输入点击确定
    def gateway_no_name(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_id(excel.id_con('item_gateway_center_setting')).click()  # 点击网关设置
        time.sleep(2)
        self.find_id(excel.id_con('item_gateway_setting_name')).click()  # 点击网关昵称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys('')  # 不输入
        self.find_id(excel.id_con('dialog_btn_positive')).click()
        return self.find_item('修改昵称')

    # 35、网关设置-修改密码
    def change_password(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.modify_gateway_password('qazwsx1234', 'wl123456789')
        return self.find_toast('重置密码成功')

    # 36、网关设置-修改密码-未填写原始密码
    def change_no_old_password(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.modify_gateway_password('', '123456789')  # 原始密码为空
        return self.find_id(excel.id_con('confirm_pwd_button')).is_enabled()  # 验证确定按钮是否可点击

    # 37、网关设置-修改密码-未填写新密码
    def change_no_new_password(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.modify_gateway_password('qazwsx1234', '')  # 新密码为空
        return self.find_id(excel.id_con('confirm_pwd_button')).is_enabled()  # 验证确定按钮是否可点击

    # 38、网关设置-修改密码-错错的原始密码，toast提示：修改失败
    def change_wrong_old_password(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.modify_gateway_password('qazwsx234', 'wl3456789')  # 错误的原始密码
        return self.find_toast('修改失败')

    # 39、网关设置-修改密码-新密码全数字，toast提示：密码至少有数字、字母或符号的2种组合
    def change_number_password(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.modify_gateway_password('qazwsx1234', '123456789')  # 新密码全部数字
        return self.find_toast('密码至少有数字、字母或符号的2种组合')

    # 40、网关设置-修改密码-新密码全字母，toast提示：密码至少有数字、字母或符号的2种组合
    def change_letter_password(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.modify_gateway_password('qazwsx1234', 'shgdjdkju')  # 新密码全部字母
        return self.find_toast('密码至少有数字、字母或符号的2种组合')

    # 41、网关设置-修改密码-新密码小于6位，toast提示：密码长度不能小于6个字符
    def change_password_6(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.modify_gateway_password('qazwsx1234', 'wl1234')  # 新密码少于8位数
        return self.find_toast('密码长度不能小于8个字符')

    # 42、网关设置-修改密码-新密码与原始密码相同，toast提示：新密码不能和老密码相同
    def change_same_password(self):
        self.old_gateway_center()  # 账号登陆，如果未绑定网关，绑定网关
        self.modify_gateway_password('qazwsx1234', 'qazwsx1234')  # 新密码与老密码一样
        return self.find_toast('新密码不能和老密码相同')
