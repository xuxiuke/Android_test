# -*- coding: utf-8 -*-
import unittest

from test_interfacecase.public.ent_playMusic import ent_playMusic


#ent接口-播放音乐接口
class test_ent_playMusic(unittest.TestCase):
    def setUp(self):
        self.ent_playMusic=ent_playMusic()

    #1、播放音乐接口
    @unittest.skip
    def test_play_music(self):
        u""""播放音乐接口"""
        self.assertEqual(self.ent_playMusic.playMusic(), "0")

    #2、查询播放列表
    def test_music_list(self):
        u""""查询播放列表"""
        self.assertEqual(self.ent_playMusic.musicList(),"0")

    #3、播放下一首或下一首
    @unittest.skip
    def test_nextOrLast(self):
        u""""播放下一首或下一首"""
        self.assertEqual(self.ent_playMusic.nextOrLast(),"0")

    #4、获取播放模式
    @unittest.skip
    def test_getPlayMode(self):
        u""""获取播放模式"""
        self.assertEqual(self.ent_playMusic.getPlayMode(),"0")


    # 5、获取内容分类
    def test_getCategoriesList(self):
        u""""获取内容分类"""
        self.assertEqual(self.ent_playMusic.getCategoriesList(), "0")


    #6、设置播放模式
    def test_setPlayMode(self):
        u""""设置播放模式"""
        self.assertEqual(self.ent_playMusic.setPlayMode(),"0")

    #7、调整播放状态
    @unittest.skip
    def test_setPlayStatus(self):
        u""""调整播放状态"""
        self.assertEqual(self.ent_playMusic.setPlayStatus(),"0")


    def tearDown(self):
        self.ent_playMusic = None


if __name__ == "__main__":
    unittest.main()