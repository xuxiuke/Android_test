# coding=utf-8

import os
import unittest, doctest
from test_interfacecase.unite import *
import HTMLTestRunner
from test_interfacecase.send_email import send_email
from test_interfacecase.unite.test_ent_playMusic import test_ent_playMusic

suite = doctest.DocTestSuite()
suite.addTest(unittest.makeSuite(test_login_byphone.Login_byphoneTestCase))  # 登录 ok
suite.addTest(unittest.makeSuite(test_login_byemail.Login_byemailTestCase))  # 邮箱登录ok
suite.addTest(unittest.makeSuite(test_reg_phonecode.Reg_phonecodeTestCase))  # 验证码发送ok
suite.addTest(unittest.makeSuite(test_token_mqtt.Token_mqttTestCase))  # 登录+退出OK
# suite.addTest(unittest.makeSuite(test_login_bythird.Login_bythirdTestCase))  #QQ人来人往登录 ok
suite.addTest(unittest.makeSuite(test_reg_byemailcode.Reg_byemailcodeTestCase))  # 4213邮箱发送ok
# suite.addTest(unittest.makeSuite(test_reg_bythird.Reg_bythirdTestCase))   # 缺少删除接口和解除三方绑定接口
suite.addTest(unittest.makeSuite(test_terminal_reg_android.Terminal_reg_addroidTestCase))  # 注册安卓设备OK
suite.addTest(unittest.makeSuite(test_terminal_reg_ios.Terminal_reg_iosTestCase))  # 注册ios设备OK
suite.addTest(unittest.makeSuite(test_login_third_bind.Login_thirdbindTestCase))  # 微信绑定 可_能脏OK
suite.addTest(unittest.makeSuite(test_login_bythird_wechat.Login_bythird_wechatTestCase))  # 微信登录 可能脏OK
suite.addTest(unittest.makeSuite(test_user_third_unbind.User_third_unbindTestCase))  # 微信解绑  纯解绑用手机号登录的 ok
suite.addTest(unittest.makeSuite(test_login_third_update.Login_third_updateTestCase))  # 三方换绑 ok
suite.addTest(unittest.makeSuite(test_user_third_get.User_third_getTestCase))  # 获取三方绑定结果 OK
suite.addTest(unittest.makeSuite(test_user_third_bind.User_third_bindTestCase))  # 微信绑定  ok
suite.addTest(unittest.makeSuite(test_user_third_bind_phonecode.User_third_bind_phonecodeTestCase))  # 三方账号绑定手机号 ok
suite.addTest(unittest.makeSuite(test_user_third_unbind.User_third_unbindTestCase))  # 微信解绑 ok
# suite.addTest(unittest.makeSuite(test_feedback_saveFeedback.Feedback_saveFeedbackTestCase))  # 反馈意见OK
suite.addTest(unittest.makeSuite(test_user_updatepass_phonecode.User_updatepass_phonecodeTestCase))  # 修改密码ok
suite.addTest(unittest.makeSuite(test_user_info_update.User_info_updateTestCase))  # 修改用户信息ok
suite.addTest(unittest.makeSuite(test_user_update_phone_phonecode.User_update_phone_phonecodeTestCase))  # OK
suite.addTest(unittest.makeSuite(test_user_email_update.User_email_updateTestCase))  # OK
suite.addTest(unittest.makeSuite(test_user_update_email_oldemailcode.User_update_email_oldemailcodeTestCase))  # ok
# suite.addTest(unittest.makeSuite(test_user_phone_update.User_phone_updateTestCase))  #等待需要王雷的删除接口
suite.addTest(unittest.makeSuite(test_user_update_phone_oldphonecode.User_update_phone_oldphonecodeTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_update_phone_verifyoldphone.User_update_phone_verifyoldphoneTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_updatepass_email.User_updatepass_emailTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_info.User_infoTestCase))  # ok
suite.addTest(unittest.makeSuite(test_app_getAppInfo.App_getAppInfoTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices.Users_uId_devicesTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_sip.Users_uId_sipTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_deviceId_bound.Users_uId_devices_deviceId_boundTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_staticInfo.Users_uId_devices_staticInfoTestCase))  # ok
suite.addTest(unittest.makeSuite(test_records_uId_devices_deviceId.Records_uId_devices_deviceIdTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_deviceId.Users_uId_devices_deviceIdTestCase))  # ok
suite.addTest(unittest.makeSuite(
    test_users_uId_device_relation_deviceId_delete.Users_uId_device_relation_deviceId_deleteTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_device_relation.Users_uId_device_relationTestCase))  # ok
suite.addTest(
    unittest.makeSuite(test_users_uId_device_relation_deviceId.Users_uId_device_relation_deviceIdTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_users_push_info.Users_uId_users_push_infoTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_users_push_info_get.Users_uId_users_push_info_getTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_users_push_info_delete.Users_uId_users_push_info_deleteTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_third_devices.Users_uId_third_devicesTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_alarm_Details.Users_uId_devices_alarm_DetailsTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_resource_token.Users_uId_devices_resource_tokenTestCase))  # ok
suite.addTest(
    unittest.makeSuite(test_users_uId_devices_resource_token1.Users_uId_devices_resource_token1TestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_info.Users_uId_devices_infoTestCase))  # ok
suite.addTest(unittest.makeSuite(
    test_users_uId_check_deviceId_v6_supportOrNot.Users_uId_check_deviceId_v6_supportOrNotTestCase))  # ok
suite.addTest(unittest.makeSuite(
    test_users_uId_check_deviceId_v6_supportOrNot_non.Users_uId_check_deviceId_v6_supportOrNot_nonTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_member_sign_info.User_member_sign_infoTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_member_point_info.User_member_point_infoTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_member_point_history.User_member_point_historyTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_member_sign.User_member_signTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_grant.Users_uId_devices_grantTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_grant_deviceId.Users_uId_devices_grant_deviceIdTestCase))  # ok
suite.addTest(unittest.makeSuite(
    test_users_uId_devices_grant_deviceId_granteeUid.Users_uId_devices_grant_deviceId_granteeUidTestCase))  # ok
suite.addTest(unittest.makeSuite(test_widget_getUserWidgetInfo.Widget_getUserWidgetInfoTestCase))  # ok
suite.addTest(unittest.makeSuite(test_widget_getUserWidgetInfo_non.Widget_getUserWidgetInfo_nonTestCase))  # ok
suite.addTest(
    unittest.makeSuite(test_users_uId_devices_deleteAlarmInfo.Users_uId_devices_deleteAlarmInfoTestCase))  # ok
suite.addTest(
    unittest.makeSuite(test_users_uId_devices_deleteAlarmInfo_msg.Users_uId_devices_deleteAlarmInfo_msgTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_users_devices_verify.Users_uId_users_devices_verifyTestCase))  # ok
suite.addTest(unittest.makeSuite(test_theme_getAllTheme.Theme_getAllThemeTestCase))  # ok
suite.addTest(unittest.makeSuite(
    test_records_uId_devices_deviceId_statistics_CO2.Records_uId_devices_deviceId_statistics_CO2TestCase))  # ok
suite.addTest(unittest.makeSuite(
    test_records_uId_devices_deviceId_statistics_humiture.Records_uId_devices_deviceId_statistics_humitureTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_alarms.Users_uId_devices_alarmsTestCase))  # ok
suite.addTest(unittest.makeSuite(test_users_uId_devices_alarms_logs.Users_uId_devices_alarms_logsTestCase))  # ok
suite.addTest(unittest.makeSuite(
    test_users_uId_devices_deviceId_bound_relation_code.Users_uId_devices_deviceId_bound_relation_codeTestCase))  # ok
suite.addTest(unittest.makeSuite(
    test_users_uId_rememberCurrentDevice_verfyPassword.Users_uId_rememberCurrentDevice_verfyPasswordTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_bindthird_phonecode.User_bindthird_phonecode))  # ok
suite.addTest(
    unittest.makeSuite(test_user_updatepass_byphone.User_updatepass_byphoneTestCase))  # changepassword 写死  #ok 没挂
suite.addTest(unittest.makeSuite(
    test_user_updatepass.User_updatepassTestCase))  # 通过调用user/updatepass/byphone改回密码，用sso_post_headers方法 # 没挂断
suite.addTest(unittest.makeSuite(
    test_users_uId_devices_deviceId_getChildDevices.Users_uId_devices_deviceId_getChildDevicesTestCase))  # ok
suite.addTest(unittest.makeSuite(test_login_phone_email_sendCode.Login_phone_email_sendCodeTestCase))  # ok
suite.addTest(unittest.makeSuite(test_login_phone_email_login.Login_phone_email_loginTestCase))  # ok
suite.addTest(unittest.makeSuite(test_luban_adv_info.Luban_adv_infoTestCase))  # ok
suite.addTest(unittest.makeSuite(test_user_wechat_bind_phonecode.User_wechat_bind_phonecodeTestCase))  # 物联公众号绑定V6账号发验证码
suite.addTest(unittest.makeSuite(test_user_wechat_bind.User_wechat_bindTestCase))  # 物联公众号绑定V6账号
suite.addTest(unittest.makeSuite(test_user_wechat_update.User_wechat_updateTestCase))  # 物联公众号替换绑定 18512530681
suite.addTest(unittest.makeSuite(
    test_user_wechat_update_recover.User_wechat_update_recoverTestCase))  # 物联公众号解除绑定V6账号  写死  18512530681
suite.addTest(unittest.makeSuite(test_area_province.Area_provinceTestCase))  # 查询区域接口
suite.addTest(unittest.makeSuite(test_slideshow_getAllSlides.Slideshow_getAllSlidesTestCase))  # 查询banner列表
suite.addTest(unittest.makeSuite(test_users_uId_saveDeviceKeyValue.Users_uId_saveDeviceKeyValueTestCase))  # 保存设备键值对信息
suite.addTest(unittest.makeSuite(test_users_uId_getDeviceKeyValue.Users_uId_getDeviceKeyValueTestCase))  # 查询设备键值对信息
suite.addTest(unittest.makeSuite(test_users_uId_user_push.Users_uId_user_pushTestCase))  # 通知WiFi设备绑定的用户，有人正绑定他的设备
suite.addTest(
    unittest.makeSuite(test_users_uId_getBcCameraId.Users_uId_getBcCameraIdTestCase))  # 通知WiFi设备绑定的用户，有人正绑定他的设备
suite.addTest(unittest.makeSuite(test_users_uId_oss_ram_account.Users_uId_oss_ram_accountTestCase))  # 获取爱看OSS子账号数据
suite.addTest(unittest.makeSuite(test_area_city.Area_cityTestCase))  # 查询城市接口
suite.addTest(unittest.makeSuite(test_das_weather_current.Das_weather_currentTestCase))  # 查询城市的天气温湿度接口
suite.addTest(unittest.makeSuite(test_ent_playMusic))  # ent接口，向往音箱测试

resultname = os.path.join(os.getcwd() + '\\' + 'wuliancloud_interfacetest.html')  # 'result.html'
file_result = open(resultname, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title="物联云接口测试报告", description="用例执行情况:")
# runner=HTMLTestReportCN.HTMLTestRunner(stream = file_result, title = "物联云接口测试报告", description = "用例执行情况:",tester="赵永健")
runner.run(suite)
send_email()
file_result.close()
