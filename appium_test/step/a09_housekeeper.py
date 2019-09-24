# coding=utf-8

"""
Created on 2018年10月17日

@author: Duke    管家
"""

from appium_test.PO import base_page
from PO import excel
import time

class Housekeeper(base_page.Action):

    # 前提条件，管家，删除所有管家
    def mine_housekeeper(self):
        self.old_gateway()  # 账号登陆，绑定网关
        self.driver.back()
        time.sleep(1)
        self.find_id(excel.id_con('scene_name')).click()  # 点击我的管家
        self.wait_ac(excel.activity_con('housekeeper_activity'))
        time.sleep(1)
        while True:
            if self.is_element('xpath', excel.xpath_con('housekeeper_list')):  # 验证是否有场景任务
                self.leftswip_housekeeper(2000)  # 左划任务
                time.sleep(1)
                self.find_xpath(excel.xpath_con('housekeeper_delete')).click()  # 点击删除按钮
                time.sleep(1)
            else:
                break

    # 管家，进入我的管家页面
    def housekeeper_page(self):
        self.old_gateway()  # 账号登陆，绑定网关
        self.driver.back()
        time.sleep(1)
        self.find_id(excel.id_con('scene_name')).click()  # 点击我的管家
        return self.wait_ac(excel.activity_con('housekeeper_activity'))

    # 管家-我的管家页面，没有任务情况，提示：还没有创建管家任务，点击右上角“+”创建(实际有BUG)
    def no_housekeeper(self):
        self.mine_housekeeper()  # 我的管家页面，删除所有管家任务
        return self.find_item('还没有创建管家任务，点击右上角“+”创建')

    # 管家-我的管家页面，点击右上角“+”，弹出创建管家任务编辑框
    def add_housekeeper(self):
        self.mine_housekeeper()  # 我的管家页面，删除所有管家任务
        self.find_xpath(excel.xpath_con('housekeeper_add')).click()  # 点击右上+按钮
        time.sleep(1)
        return self.find_item('创建管家任务')

    # 管家-我的管家页面，点击右上角“+”，弹出创建管家任务编辑框，点击右上“x”，编辑框消失
    def add_housekeeper_x(self):
        self.add_housekeeper()  # 创建管家任务编辑框页面
        self.find_xpath(excel.xpath_con('create_housekeeeper_x')).click()  # 点击右上X按钮
        time.sleep(1)
        return self.find_item('创建管家任务')

    # 管家-创建管家任务编辑框，点击定时任务，进入定时任务编辑页面，查找：当时间到达-------------------------------------------------
    def timing_editpage(self):
        self.add_housekeeper()  # 创建管家任务编辑框页面
        self.find_xpath(excel.xpath_con('create_housekeeeper_timing')).click()  # 点击定时任务
        time.sleep(1)
        return self.find_item('当时间到达')

    # 管家-定时任务编辑页面，点击名称，弹出名称弹窗
    def timing_name(self):
        self.timing_editpage()  # 定时任务编辑页面
        self.find_xpath(excel.xpath_con('timing_name')).click()  # 点击名称
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('timing_name_search'))  # 验证是否有名称弹窗

    # 管家-定时任务编辑-名称弹窗，输入名称呵呵123，点击确定，弹窗消失，名称显示为：呵呵123
    def timing_name_sure(self):
        self.timing_name()  # 定时任务，名称弹窗
        self.find_xpath(excel.xpath_con('renameInput')).send_keys(u'呵呵123')  # 名称输入框输入新名称 呵呵123
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(1)
        return self.find_item('呵呵123')

    # 管家-定时任务编辑-名称弹窗，输入名称呵呵123，点击取消，弹窗消失，名称显示未变
    def timing_name_cancel(self):
        self.timing_name()  # 定时任务，名称弹窗
        self.find_xpath(excel.xpath_con('renameInput')).send_keys(u'呵呵123')  # 名称输入框输入新名称 呵呵123
        time.sleep(1)
        self.find_xpath(excel.xpath_con('addDelay_cancel')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('呵呵123')

    # 管家-定时任务编辑页面，点击时间，进入定时编辑页面，查找Sun
    def timing_time(self):
        self.timing_editpage()  # 定时任务编辑页面
        self.find_xpath(excel.xpath_con('timing_time')).click()  # 点击事件
        time.sleep(1)
        return self.find_item('Sun')

    # 管家-定时编辑页面，点击保存，跳转定时任务编辑页面
    def timing_time_save(self):
        self.timing_time()  # 定时任务，定时编辑页面
        self.find_xpath(excel.xpath_con('timeTask1_save')).click()  # 点击保存按钮
        time.sleep(1)
        return self.find_item('当时间到达')

    # 管家-定时任务编辑页面，点击执行以下任务，进入添加任务页面，查找添加要执行的设备
    def timetask_page(self):
        self.timing_name_sure()  # 定时任务编辑页面，已设置名称为呵呵123
        self.find_xpath(excel.xpath_con('timing_tasks')).click()  # 点击执行以下任务
        time.sleep(1)
        return self.find_item('添加要执行的设备')

    # 管家-添加任务页面，点击添加要执行的设备，进入选择设备页面
    def timetask_device_page(self):
        self.timetask_page()  # 添加任务页面
        self.find_xpath(excel.xpath_con('circumstances_needdodevice')).click()  # 点击添加要执行的设备
        time.sleep(1)
        return self.find_item('选择设备')

    # 管家-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def timetask_allzone(self):
        self.timetask_device_page()  # 定时任务，选择设备页面
        self.find_xpath(excel.xpath_con('device_list_allAreas')).click()  # 点击全部分区
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('all_zone'))  # 延时是否有全部分区元素

    # 管家-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def timetask_allclass(self):
        self.timetask_device_page()  # 定时任务，选择设备页面
        self.find_xpath(excel.xpath_con('device_list_Categories')).click()  # 点击全部分类
        time.sleep(1)
        return self.find_item('智能门锁')

    # 管家-选择设备页面，点击批量添加，进入批量添加页面，查找全选
    def timetask_alladd(self):
        self.timetask_device_page()  # 定时任务，选择设备页面
        self.find_xpath(excel.xpath_con('batchAdd')).click()  # 点击批量添加
        time.sleep(1)
        return self.find_item('全选')

    # 管家-添加任务页面，点击添加要执行的场景，进入选择场景页面
    def timetask_scene_page(self):
        self.timetask_page()  # 添加任务页面
        self.find_xpath(excel.xpath_con('circumstances_needdoscene')).click()  # 点击添加要执行的场景
        time.sleep(1)
        return self.find_item('选择场景')

    # 管家-添加任务页面，点击添加要执行的场景，进入选择场景页面，点击完成，toast提示：请选择一个场景，H5页面定位不了toast
    def timetask_scene_finish(self):
        self.timetask_scene_page()  # 选择场景页面
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击右上完成按钮
        return self.find_item('选择场景')

    # 管家-选择设备页面，点击墙面插座，进入设置设备状态页面
    def setting_device_status_page(self):
        self.timetask_device_page()  # 选择设备页面
        self.find_xpath(excel.xpath_con('socket_5')).click()
        time.sleep(1)
        return self.find_item('设置设备状态')

    # 管家-设置设备状态页面，点击开，进入添加延时任务页面
    def delay_task_page(self):
        self.setting_device_status_page()  # 设置设备状态页面
        self.find_xpath(excel.xpath_con('socket_open')).click()  # 点击开
        time.sleep(1)
        return self.find_item('添加延时')

    # 管家-添加延时任务页面，点击打开添加延时按钮，弹出延时时间编辑框，查找秒
    def delay_task_tiemopen(self):
        self.delay_task_page()  # 添加延时页面
        self.find_xpath(excel.xpath_con('delay_close')).click()  # 点击打开添加延时开关按钮
        time.sleep(1)
        return self.find_item('秒')

    # 管家-添加延时任务页面，点击打开添加延时按钮，再次点击按钮，延时时间编辑框隐藏，查找不到秒
    def delay_task_timeclose(self):
        self.delay_task_tiemopen()  # 添加延时页面，延时开关打开状态
        self.find_xpath(excel.xpath_con('delay_open')).click()  # 点击关闭添加延时开关按钮
        time.sleep(1)
        return self.find_item('秒')

    # 管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面
    def delay_task_finish(self):
        self.delay_task_page()  # 添加延时页面
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        time.sleep(1)
        return self.find_item('墙面插座')

    # 管家-添加延时任务页面，左划任务，拉出删除按钮
    def task_leftswip(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.leftswip_delaytask(2000)  # 左划执行任务
        return self.find_item('删除')

    # 管家-添加延时任务页面，左划任务，拉出删除按钮，点击删除按钮，任务删除
    def task_delete(self):
        self.task_leftswip()  # 添加执行任务，左划拉出删除按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('ediescene_delete')).click()  # 点击删除按钮
        time.sleep(1)
        return self.find_item('墙面插座')

    # 管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗
    def giveup_edit(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.find_xpath(excel.xpath_con('back')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('giveup_edit'))  # 验证是否有弹窗

    # 管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗，点击取消，弹窗消失
    def giveup_edit_cancel(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.find_xpath(excel.xpath_con('back')).click()  # 点击左上返回按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('giveup_edit_cancel')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('giveup_edit'))  # 验证是否有弹窗

    # 管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗，点击确定，跳转我的管家页面，任务未保存
    def giveup_edit_sure(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.find_xpath(excel.xpath_con('back')).click()  # 点击左上返回按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('giveup_edit_sure')).click()  # 点击确定按钮
        time.sleep(1)
        return self.find_item('呵呵123')  # 跳转我的管家页面，管家任务没有保存

    # 管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击保存按钮，跳转我的页面，定时任务保存成功，查找呵呵123
    def timed_task(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.find_xpath(excel.xpath_con('timeTask1_save')).click()  # 点击右上保存按钮
        time.sleep(2)
        return self.find_item('呵呵123')

    # 管家-定时任务编辑页面，点击保存按钮，弹窗提示：执行任务不能为空，请添加
    def timed_notask(self):
        self.timing_editpage()  # 管家定时任务编辑页面
        self.find_xpath(excel.xpath_con('timeTask1_save')).click()  # 点击右上保存按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 判断是否有弹窗这个元素

    # 管家-定时任务编辑页面，点击保存按钮，弹窗提示：执行任务不能为空，请添加，点击确定按钮，弹窗消失
    def timed_notask_sure(self):
        self.timed_notask()  # 管家-定时任务-执行任务不能为空弹窗
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 判断是否有弹窗这个元素

    # 管家-新建一个定时任务，点击任务，进入定时任务编辑页面
    def click_timedtask(self):
        self.timed_task()  # 创建一个定时任务
        self.find_xpath(excel.xpath_con('housekeeper_list')).click()  # 点击第一个管家
        time.sleep(2)
        return self.find_item('当时间到达')

    # 管家-新建一个定时任务，左划任务，拉出编辑按钮
    def swip_timedtask(self):
        self.timed_task()  # 创建一个定时任务
        self.leftswip_housekeeper(2000)  # 左划第一个管家任务
        return self.find_item('编辑')

    # 管家-新建一个定时任务，左划任务，拉出编辑按钮，点击编辑按钮，进入定时任务编辑页面
    def swip_timedtask_edit(self):
        self.swip_timedtask()  # 左划管家任务，拉出编辑按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('housekeeper_edit')).click()  # 点击编辑按钮
        time.sleep(2)
        return self.find_item('当时间到达')

    # 管家-新建一个定时任务，左划任务，拉出删除按钮
    def swip_timedtask_delete(self):
        self.timed_task()  # 创建一个定时任务
        self.leftswip_housekeeper(2000)  # 左划第一个管家任务
        return self.find_item('删除')

    # 管家-新建一个定时任务，左划任务，拉出删除按钮，点击删除按钮，任务被删除
    def swip_timedtask_deletesure(self):
        self.swip_timedtask_delete()  # 左划任务，拉出删除按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('housekeeper_delete')).click()  # 点击删除按钮
        time.sleep(2)
        return self.find_item('呵呵123')

    # 管家-创建管家任务编辑框，点击情景任务，进入情景任务编辑页面-----------------------------------------------------------------
    def scenetask_page(self):
        self.add_housekeeper()  # 创建管家任务编辑框页面
        self.find_xpath(excel.xpath_con('create_housekeeeper_scene')).click()  # 点击情景任务
        time.sleep(1)
        return self.find_item('满足任一条件时')

    # 管家-情景任务编辑页面，点击名称，弹出名称弹窗
    def scenetask_name(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_xpath(excel.xpath_con('timing_name')).click()  # 点击名称
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('timing_name_search'))  # 验证是否有名称弹窗

    # 管家-情景任务编辑-名称弹窗，输入名称哈哈123，点击确定，弹窗消失，名称显示为：哈哈123
    def scenetask_namesure(self):
        self.scenetask_name()  # 情景任务编辑页面，名称弹窗
        self.find_xpath(excel.xpath_con('renameInput')).send_keys(u'哈哈123')  # 输入名称哈哈123
        time.sleep(1)
        self.find_xpath(excel.xpath_con('giveup_edit_sure')).click()  # 点击确定按钮
        time.sleep(1)
        return self.find_item('哈哈123')

    # 管家-情景任务编辑-名称弹窗，输入名称哈哈123，点击取消，弹窗消失，名称显示未变
    def scenetask_namecancel(self):
        self.scenetask_name()  # 情景任务编辑页面，名称弹窗
        self.find_xpath(excel.xpath_con('renameInput')).send_keys(u'哈哈123')  # 输入名称哈哈123
        time.sleep(1)
        self.find_xpath(excel.xpath_con('giveup_edit_cancel')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('哈哈123')

    # 管家-情景任务编辑，点击满足任一条件时，进入选择设备页面
    def condition_page(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_xpath(excel.xpath_con('scenetask_condition')).click()  # 点击满足任一条件时
        time.sleep(1)
        return self.find_item('全部分区')

    # 管家-条件任务-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def conditionpage_zone(self):
        self.condition_page()  # 情景任务-条件任务，选择设备页面
        self.find_xpath(excel.xpath_con('device_list_allAreas')).click()  # 点击全部分区
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('all_zone'))  # 验证是否存在元素全部分区

    # 管家-条件任务-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def conditionpage_category(self):
        self.condition_page()  # 情景任务-条件任务，选择设备页面
        self.find_xpath(excel.xpath_con('device_list_Categories')).click()  # 点击全部分类
        time.sleep(1)
        return self.find_item('智能门锁')

    # 管家-条件任务-选择设备页面，点击门窗磁探测器，进入设置设备状态页面
    def condition_mannetic_page(self):
        self.condition_page()  # 情景任务-条件任务，选择设备页面
        self.find_xpath(excel.xpath_con('magnetic_4')).click()  # 点击门窗磁探测器
        time.sleep(1)
        return self.find_item('设置设备状态')

    # 管家-条件任务-设置设备状态页面，点击被打开，跳转情景任务编辑页面，查找门窗磁探测器
    def condition_magnetic_open(self):
        self.condition_mannetic_page()  # 管家-条件任务-门磁设置设备状态页面
        self.find_xpath(excel.xpath_con('magnetic_open')).click()  # 点击被打开
        time.sleep(1)
        return self.find_item('门窗磁探测器')

    # 管家-条件任务-设置设备状态页面，点击被关闭，跳转情景任务编辑页面，查找门窗磁探测器
    def condition_magnetic_close(self):
        self.condition_mannetic_page()  # 管家-条件任务-门磁设置设备状态页面
        self.find_xpath(excel.xpath_con('magnetic_close')).click()  # 点击被关闭
        time.sleep(1)
        return self.find_item('门窗磁探测器')

    # 管家-条件任务成功-情景任务编辑页面，左划任务，拉出删除按钮，查找删除
    def condition_swip(self):
        self.condition_magnetic_open()  # 创建一个条件任务
        self.leftswip_condition(2000)  # 左划条件任务
        time.sleep(1)
        return self.find_item('删除')

    # 管家-条件任务成功-情景任务编辑页面，左划任务，拉出删除按钮，查找删除，点击删除，任务删除成功，查找不到门窗磁探测器
    def condition_swip_delete(self):
        self.condition_swip()  # 左划条件任务拉出删除按钮
        self.find_xpath(excel.xpath_con('ediescene_delete')).click()  # 点击删除按钮
        time.sleep(1)
        return self.find_item('门窗磁探测器')

    # 管家-情景任务编辑，点击执行以下任务，情景任务页面，查找添加要执行的设备
    def implement_page(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_xpath(excel.xpath_con('scenetask_task')).click()  # 点击执行以下任务
        time.sleep(1)
        return self.find_item('添加要执行的设备')

    # 管家-执行任务-情景任务页面，点击添加要执行的设备，进入选择设备页面
    def implement_devicepage(self):
        self.implement_page()  # 执行任务-情景任务页面
        self.find_xpath(excel.xpath_con('circumstances_needdodevice')).click()  # 点击添加要执行的设备
        time.sleep(1)
        return self.find_item('选择设备')

    # 管家-执行任务-情景任务页面，点击添加要执行的场景，进入选择场景页面
    def implement_scenepage(self):
        self.implement_page()  # 执行任务-情景任务页面
        self.find_xpath(excel.xpath_con('circumstances_needdoscene')).click()  # 点击添加要执行的场景
        time.sleep(1)
        return self.find_item('选择场景')

    # 管家-执行任务-情景任务页面，点击添加要执行的场景，进入选择场景页面，点击完成，toast提示：请选择一个场景
    def implement_scenepage_finish(self):
        self.implement_scenepage()  # 情景任务-选择场景，场景选择页面
        self.find_xpath(excel.xpath_con('finishState')).click()  # 点击完成按钮
        time.sleep(1)
        return self.find_item('选择场景')

    # 管家-执行任务-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def implement_device_zone(self):
        self.implement_devicepage()  # 执行任务-选择设备页面
        self.find_xpath(excel.xpath_con('device_list_allAreas')).click()  # 点击全部分区
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('all_zone'))  # 验证是否存在元素全部分区

    # 管家-执行任务-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def implement_device_categroy(self):
        self.implement_devicepage()  # 执行任务-选择设备页面
        self.find_xpath(excel.xpath_con('device_list_Categories')).click()  # 点击全部分类
        time.sleep(1)
        return self.find_item('智能门锁')

    # 管家-执行任务-选择设备页面，点击批量添加，进入批量添加页面，查找全选
    def implement_device_add(self):
        self.implement_devicepage()  # 执行任务-选择设备页面
        self.find_xpath(excel.xpath_con('batchAdd')).click()  # 点击批量添加
        time.sleep(1)
        return self.find_item('全选')

    # 管家-执行任务-选择设备页面，点击墙面插座，进入设置设备状态页面
    def implement_socket_setting(self):
        self.implement_devicepage()  # 执行任务-选择设备页面
        self.find_xpath(excel.xpath_con('socket_5')).click()  # 点击墙面插座
        time.sleep(1)
        return self.find_item('设置设备状态')

    # 管家-执行任务-设置设备状态页面，点击开，跳转添加延时页面
    def implement_socket_open(self):
        self.implement_socket_setting()  # 情景任务-执行任务，墙面插座设置设备状态页面
        self.find_xpath(excel.xpath_con('socket_open')).click()  # 点击墙面插座开
        time.sleep(1)
        return self.find_item('添加延时')

    # 管家-执行任务-设置设备状态页面，点击关，跳转添加延时页面
    def implement_socket_close(self):
        self.implement_socket_setting()  # 情景任务-执行任务，墙面插座设置设备状态页面
        self.find_xpath(excel.xpath_con('socket_close')).click()  # 点击墙面插座关
        time.sleep(1)
        return self.find_item('添加延时')

    # 管家-执行任务-添加延时页面，点击添加延时开关按钮，弹出延时时间编辑框，查找秒
    def implement_time_open(self):
        self.implement_socket_open()  # 情景任务-执行任务，添加延时页面
        self.find_xpath(excel.xpath_con('delay_close')).click()  # 点击打开延时开关
        time.sleep(1)
        return self.find_item('秒')

    # 管家-执行任务-添加延时页面，点击添加延时开关按钮，弹出延时时间编辑框，再次点击开关按钮，延时时间编辑框隐藏，查找不到秒
    def implement_time_close(self):
        self.implement_time_open()  # 打开延时按钮
        self.find_xpath(excel.xpath_con('delay_open')).click()  # 点击关闭延时开关
        time.sleep(1)
        return self.find_item('秒')

    # 管家-执行任务-添加延时页面，点击完成按钮，跳转情景任务编辑页面，查找墙面插座
    def implement_finish(self):
        self.implement_socket_open()  # 情景任务-执行任务，添加延时页面
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        time.sleep(1)
        return self.find_item('墙面插座')

    # 管家-已设置任务，点击执行任务，进入设置设备状态页面
    def implement_click_firsttask(self):
        self.implement_finish()  # 新建一个执行任务
        self.find_xpath(excel.xpath_con('implement_1')).click()  # 点击第一个执行任务
        time.sleep(1)
        return self.find_item('设置设备状态')

    # 管家-已设置任务，左划执行任务，拉出删除按钮，查找删除
    def implement_swip(self):
        self.implement_finish()  # 新建一个执行任务
        self.leftswip_implement(2000)  # 左划任务
        time.sleep(1)
        return self.find_item('删除')

    # 管家-已设置任务，左划执行任务，拉出删除按钮，点击删除按钮，任务被删除，查找墙面插座
    def implement_swip_delete(self):
        self.implement_swip()  # 左划任务，拉出删除按钮
        self.find_xpath(excel.xpath_con('ediescene_delete')).click()  # 点击删除按钮
        time.sleep(1)
        return self.find_item('墙面插座')

    # 管家-情景任务编辑页面，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加
    def condition_implement_allnone(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_xpath(excel.xpath_con('circumstances_save')).click()  # 点击保存按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 管家-情景任务编辑页面，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加，点击确定按钮，弹窗消失
    def condition_implement_allnone_sure(self):
        self.condition_implement_allnone()  # 执行条件或者执行任务不能为空弹窗
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 管家-情景任务编辑页面-已设置执行条件，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加
    def implement_none(self):
        self.condition_magnetic_open()  # 创建一个条件任务
        self.find_xpath(excel.xpath_con('circumstances_save')).click()  # 点击保存按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 管家-情景任务编辑页面-已设置执行任务，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加
    def condition_none(self):
        self.implement_finish()  # 新建一个执行任务
        self.find_xpath(excel.xpath_con('circumstances_save')).click()  # 点击保存按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 管家-已设置名称-已设置执行条件-已设置执行任务，点击保存，跳转我的管家页面，查找第一个管家任务元素
    def scenetask_creat(self):
        self.scenetask_namesure()  # 设置情景任务名称
        self.find_xpath(excel.xpath_con('scenetask_condition')).click()  # 点击满足任一条件时
        time.sleep(1)
        self.find_xpath(excel.xpath_con('magnetic_4')).click()  # 点击门窗磁探测器
        time.sleep(1)
        self.find_xpath(excel.xpath_con('magnetic_open')).click()  # 点击被打开
        time.sleep(1)
        self.find_xpath(excel.xpath_con('scenetask_task')).click()  # 点击执行以下任务
        time.sleep(1)
        self.find_xpath(excel.xpath_con('circumstances_needdodevice')).click()  # 点击添加要执行的设备
        time.sleep(1)
        self.find_xpath(excel.xpath_con('socket_5')).click()  # 点击墙面插座
        time.sleep(1)
        self.find_xpath(excel.xpath_con('socket_open')).click()  # 点击墙面插座开
        time.sleep(1)
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('circumstances_save')).click()  # 点击保存按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('housekeeper_list'))  # 验证元素是否存在

    # 管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑
    def giveup_edit2(self):
        self.implement_finish()  # 新建一个执行任务
        self.find_xpath(excel.xpath_con('back')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('giveup_edit'))  # 验证是否有弹窗

    # 管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑，点击取消，弹窗消失
    def giveup_edit2_cancel(self):
        self.implement_finish()  # 新建一个执行任务
        self.find_xpath(excel.xpath_con('back')).click()  # 点击左上返回按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('giveup_edit_cancel')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('giveup_edit'))  # 验证是否有弹窗

    # 管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑，点击确定，跳转我的管家页面，任务未保存
    def giveup_edit2_sure(self):
        self.implement_finish()  # 新建一个执行任务
        self.find_xpath(excel.xpath_con('back')).click()  # 点击左上返回按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('giveup_edit_sure')).click()  # 点击确定按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('housekeeper_list'))  # 验证我的管家页面管家任务元素是否存在

    # 管家-情景任务编辑页面，点击生效条件，进入生效条件页面,查找：生效时间条件
    def precondition_page(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_xpath(excel.xpath_con('conditionAdd')).click()  # 点击生效条件
        time.sleep(1)
        return self.find_item('生效时间条件')

    # 管家-生效条件页面，点击生效时间条件，进入生效时段页面
    def precondition_time(self):
        self.precondition_page()  # 生效条件页面
        self.find_xpath(excel.xpath_con('time_factor')).click()  # 点击生效时间条件
        time.sleep(1)
        return self.find_item('生效时段')

    # 管家-生效条件页面，点击生效设备条件，进入选择设备页面
    def precondition_device(self):
        self.precondition_page()  # 生效条件页面
        self.find_xpath(excel.xpath_con('device_factor')).click()  # 点击生效设备条件
        time.sleep(1)
        return self.find_item('选择设备')

    # 管家-生效条件页面，点击生效场景条件，进入选择场景页面
    def precondition_scene(self):
        self.precondition_page()  # 生效条件页面
        self.find_xpath(excel.xpath_con('Scenes_facto')).click()  # 点击生效场景条件
        time.sleep(1)
        return self.find_item('选择场景')

    # 管家-新建一个情景任务，点击情景任务，进入情景任务编辑页面
    def click_scenetask(self):
        self.scenetask_creat()  # 创建一个情景任务
        self.find_xpath(excel.xpath_con('housekeeper_list')).click()  # 点击第一个管家任务
        time.sleep(1)
        return self.find_item('满足任一条件时')

    # 管家-新建一个情景任务，左划任务，拉出编辑按钮
    def scenetask_swip_edit(self):
        self.scenetask_creat()  # 创建一个情景任务
        time.sleep(1)
        self.leftswip_housekeeper(2000)  # 左划任务
        time.sleep(1)
        return self.find_item('编辑')

    # 管家-新建一个情景任务，左划任务，拉出编辑按钮，点击编辑按钮，进入定时任务编辑页面
    def scenetask_click_edit(self):
        self.scenetask_swip_edit()  # 拉出编辑按钮
        self.find_xpath(excel.xpath_con('housekeeper_edit')).click()  # 点击编辑按钮
        time.sleep(1)
        return self.find_item('满足任一条件时')

    # 管家-新建一个情景任务，左划任务，拉出删除按钮
    def scenetask_swip_delete(self):
        self.scenetask_creat()  # 创建一个情景任务
        time.sleep(1)
        self.leftswip_housekeeper(2000)  # 左划任务
        time.sleep(2)
        return self.find_item('删除')

    # 管家-新建一个情景任务，左划任务，拉出删除按钮，点击删除按钮，任务被删除
    def scenetask_click_delete(self):
        self.scenetask_swip_delete()  # 拉出删除按钮
        self.find_xpath(excel.xpath_con('housekeeper_delete')).click()  # 点击删除按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('housekeeper_list'))  # 验证我的管家页面管家任务元素是否存在
