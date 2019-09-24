#!/bin/python
# Created by 顾洋溢
from test_interfacecase.unite import test_ent_playMusic
from test_interfacecase.unite import test_reg_byemailcode
from test_interfacecase.unite import test_app_getAppInfo
from test_interfacecase.unite import test_app_updateAppInfo
from test_interfacecase.unite import test_area_city
from test_interfacecase.unite import test_area_province
from test_interfacecase.unite import test_das_weather_current
from test_interfacecase.unite import test_feedback_saveFeedback
from test_interfacecase.unite import test_login_byemail
from test_interfacecase.unite import test_login_byphone
from test_interfacecase.unite import test_login_bythird
from test_interfacecase.unite import test_login_bythird_wechat
from test_interfacecase.unite import test_login_logout
from test_interfacecase.unite import test_login_phone_email_login
from test_interfacecase.unite import test_login_phone_email_sendCode
from test_interfacecase.unite import test_login_third_bind
from test_interfacecase.unite import test_login_third_update
from test_interfacecase.unite import test_luban_adv_info
from test_interfacecase.unite import test_records_uId_devices_deviceId
from test_interfacecase.unite import test_records_uId_devices_deviceId_statistics_CO2
from test_interfacecase.unite import test_records_uId_devices_deviceId_statistics_humiture
from test_interfacecase.unite import test_reg_phonecode
from test_interfacecase.unite import test_slideshow_getAllSlides
from test_interfacecase.unite import test_terminal_reg_android
from test_interfacecase.unite import test_terminal_reg_ios
from test_interfacecase.unite import test_theme_getAllTheme
from test_interfacecase.unite import test_token_mqtt
from test_interfacecase.unite import test_user_bindthird_phonecode
from test_interfacecase.unite import test_user_email_update
from test_interfacecase.unite import test_user_info
from test_interfacecase.unite import test_user_info_update
from test_interfacecase.unite import test_user_member_point_history
from test_interfacecase.unite import test_user_member_point_info
from test_interfacecase.unite import test_user_member_sign
from test_interfacecase.unite import test_user_member_sign_info
from test_interfacecase.unite import test_user_phone_update
from test_interfacecase.unite import test_user_third_bind
from test_interfacecase.unite import test_user_third_bind_phonecode
from test_interfacecase.unite import test_user_third_get
from test_interfacecase.unite import test_user_third_unbind
from test_interfacecase.unite import test_user_update_email_oldemailcode
from test_interfacecase.unite import test_user_update_phone_oldphonecode
from test_interfacecase.unite import test_user_update_phone_phonecode
from test_interfacecase.unite import test_user_update_phone_verifyoldphone
from test_interfacecase.unite import test_user_updatepass
from test_interfacecase.unite import test_user_updatepass_byphone
from test_interfacecase.unite import test_user_updatepass_email
from test_interfacecase.unite import test_user_updatepass_phonecode
from test_interfacecase.unite import test_user_wechat_bind
from test_interfacecase.unite import test_user_wechat_bind_phonecode
from test_interfacecase.unite import test_user_wechat_update
from test_interfacecase.unite import test_user_wechat_update_recover
from test_interfacecase.unite import test_users_uId_check_deviceId_v6_supportOrNot
from test_interfacecase.unite import test_users_uId_check_deviceId_v6_supportOrNot_non
from test_interfacecase.unite import test_users_uId_device_relation
from test_interfacecase.unite import test_users_uId_device_relation_deviceId
from test_interfacecase.unite import test_users_uId_device_relation_deviceId_delete
from test_interfacecase.unite import test_users_uId_devices
from test_interfacecase.unite import test_users_uId_devices_alarm_Details
from test_interfacecase.unite import test_users_uId_devices_alarms
from test_interfacecase.unite import test_users_uId_devices_alarms_logs
from test_interfacecase.unite import test_users_uId_devices_deleteAlarmInfo
from test_interfacecase.unite import test_users_uId_devices_deleteAlarmInfo_msg
from test_interfacecase.unite import test_users_uId_devices_deviceId
from test_interfacecase.unite import test_users_uId_devices_deviceId_bound
from test_interfacecase.unite import test_users_uId_devices_deviceId_bound_relation_code
from test_interfacecase.unite import test_users_uId_devices_deviceId_getChildDevices
from test_interfacecase.unite import test_users_uId_devices_grant
from test_interfacecase.unite import test_users_uId_devices_grant_deviceId
from test_interfacecase.unite import test_users_uId_devices_grant_deviceId_granteeUid
from test_interfacecase.unite import test_users_uId_devices_info
from test_interfacecase.unite import test_users_uId_devices_resource_token
from test_interfacecase.unite import test_users_uId_devices_resource_token1
from test_interfacecase.unite import test_users_uId_devices_staticInfo
from test_interfacecase.unite import test_users_uId_getBcCameraId
from test_interfacecase.unite import test_users_uId_getDeviceKeyValue
from test_interfacecase.unite import test_users_uId_oss_ram_account
from test_interfacecase.unite import test_users_uId_rememberCurrentDevice_verfyPassword
from test_interfacecase.unite import test_users_uId_saveDeviceKeyValue
from test_interfacecase.unite import test_users_uId_sip
from test_interfacecase.unite import test_users_uId_third_devices
from test_interfacecase.unite import test_users_uId_user_push
from test_interfacecase.unite import test_users_uId_users_devices_verify
from test_interfacecase.unite import test_users_uId_users_push_info
from test_interfacecase.unite import test_users_uId_users_push_info_delete
from test_interfacecase.unite import test_users_uId_users_push_info_get
from test_interfacecase.unite import test_widget_getUserWidgetInfo
from test_interfacecase.unite import test_widget_getUserWidgetInfo_non







# from  unite import unite test_login_byemail
# from  unite import test_login_byphone
# from  unite import test_reg_phonecode
# from  unite import test_token_mqtt
# from  unite import test_login_logout
# from  unite import test_login_bythird
# from  unite import test_reg_byemailcode
# from  unite import test_reg_bythird     # 缺少删除接口和解除三方绑定接口
# from  unite import test_terminal_reg_android
# from  unite import test_terminal_reg_ios
# from  unite import test_login_third_bind
# from  unite import test_login_bythird_wechat
# from  unite import test_user_third_unbind
# from  unite import test_login_third_update
# from  unite import test_user_third_get
# from  unite import test_user_third_bind
# from  unite import test_user_third_bind_phonecode
# from  unite import test_user_third_unbind
# from  unite import test_feedback_saveFeedback
# from  unite import test_user_updatepass_phonecode
# from  unite import test_user_info_update
# from  unite import test_user_update_phone_phonecode
# from  unite import test_user_email_update
# from  unite import test_user_update_email_oldemailcode
# from  unite import test_user_phone_update
# from  unite import test_user_update_phone_oldphonecode
# from  unite import test_user_update_phone_verifyoldphone
# from  unite import test_user_updatepass_byphone
# from  unite import test_user_updatepass_email
# from  unite import test_user_info
# from  unite import test_user_updatepass
# from  unite import test_users_uId_devices
# from  unite import test_users_uId_sip
# from  unite import test_users_uId_devices_deviceId_bound
# from  unite import test_users_uId_devices_staticInfo
# from  unite import test_records_uId_devices_deviceId
# from  unite import test_users_uId_devices_deviceId
# from  unite import test_users_uId_device_relation
# from  unite import test_users_uId_device_relation_deviceId
# from  unite import test_users_uId_device_relation_deviceId_delete
# from  unite import test_users_uId_users_push_info
# from  unite import test_users_uId_users_push_info_get
# from  unite import test_users_uId_users_push_info_delete
# from  unite import test_users_uId_third_devices
# from  unite import test_users_uId_devices_alarm_Details
# from  unite import test_users_uId_devices_resource_token
# from  unite import test_users_uId_devices_resource_token1
# from  unite import test_users_uId_devices_info
# from  unite import test_users_uId_devices_grant_deviceId
# from  unite import test_users_uId_check_deviceId_v6_supportOrNot
# from  unite import test_users_uId_check_deviceId_v6_supportOrNot_non
# from  unite import test_user_member_sign_info
# from  unite import test_user_member_point_info
# from  unite import test_user_member_point_history
# from  unite import test_user_member_sign
# from  unite import test_users_uId_devices_grant
# from  unite import test_users_uId_devices_grant_deviceId_granteeUid
# from  unite import test_widget_getUserWidgetInfo
# from  unite import test_widget_getUserWidgetInfo_non
# #from  unite import test_app_updateAppInfo
# from  unite import test_users_uId_devices_deleteAlarmInfo
# from  unite import test_users_uId_devices_deleteAlarmInfo_msg
# from  unite import test_app_getAppInfo
# from  unite import test_users_uId_users_devices_verify
# from  unite import test_theme_getAllTheme
# from  unite import test_records_uId_devices_deviceId_statistics_CO2
# from  unite import test_records_uId_devices_deviceId_statistics_humiture
# from  unite import test_users_uId_devices_alarms
# from  unite import test_users_uId_devices_alarms_logs
# from  unite import test_users_uId_devices_deviceId_bound_relation_code
# from  unite import test_users_uId_rememberCurrentDevice_verfyPassword
# from  unite import test_users_uId_devices_deviceId_getChildDevices
# from  unite import test_user_bindthird_phonecode
# from  unite import test_login_phone_email_sendCode
# from  unite import test_login_phone_email_login
# from  unite import test_luban_adv_info
# from  unite import test_user_wechat_bind_phonecode
# from  unite import test_user_wechat_bind
# from  unite import test_user_wechat_update
# from  unite import test_user_wechat_update_recover
# from  unite import test_area_province
# from  unite import test_slideshow_getAllSlides
# from  unite import test_users_uId_saveDeviceKeyValue
# from  unite import test_users_uId_getDeviceKeyValue
# from  unite import test_users_uId_user_push
# from  unite import test_users_uId_getBcCameraId
# from  unite import test_users_uId_oss_ram_account
# from  unite import test_area_city
# from  unite import test_das_weather_current