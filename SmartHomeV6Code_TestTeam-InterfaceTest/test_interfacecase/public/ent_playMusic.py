# -*- coding: utf-8 -*-

from test_interfacecase.bussiness.kernal_function import Kernal_function

# ent 接口 向往音箱接口测试
class ent_playMusic(object):
    def __init__(self):
        pass
    #播放音乐接口
    def playMusic(self):
        read_csv =Kernal_function("music/playMusic")
        return read_csv.entPostAnswer()["resultCode"]

    #查询播放列表
    def musicList(self):
        read_csv = Kernal_function("music/musicList")
        return read_csv.entGetAnswer()["resultCode"]

    #ent接口-播放下一首或下一首。
    def nextOrLast(self):
        read_csv = Kernal_function("music/nextOrLast")
        return read_csv.entPostAnswer()["resultCode"]

    #ent接口-获取播放模式.
    def getPlayMode(self):
        read_csv = Kernal_function("music/get/playMode")
        return read_csv.entGetAnswer()["resultCode"]

    #ent接口-获取内容分类
    def getCategoriesList(self):
        read_csv = Kernal_function("music/categories/list")
        return read_csv.entGetAnswer()["resultCode"]

    #ent接口-设置播放模式 。
    def setPlayMode(self):
        read_csv = Kernal_function("music/set/playMode")
        return read_csv.entPostAnswer()["resultCode"]

    #ent接口-调整播放状态。
    def setPlayStatus(self):
        read_csv = Kernal_function("music/set/play/status")
        return read_csv.entPostAnswer()["resultCode"]

    def dispose(self):
        pass