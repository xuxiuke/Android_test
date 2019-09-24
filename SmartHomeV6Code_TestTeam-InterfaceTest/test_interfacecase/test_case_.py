#coding=utf-8

import os
#列出某个文件夹下的所有case,这里用的是python，所在py文件运行一次后会生成一个pyc的副本
caselist = os.listdir('F:\\python\\test_interfacecase\\unite')
print(caselist)
for a in caselist:
    s = a.split(".")[1:][0]  # 选取py后缀的文件
    if s == 'py':
        # 此处执行dos命令并将结果保存到log.txt
        os.system('python F:\\python\\test_interfacecase\\unite\\%s 1>>log.txt 2>&1'%a)

#===2>&1的意思就是说无论标准出错在哪里(哪怕是没有?)，都将标准出错重定向到标准输出中。
#===2>就是将标准出错重定向到某个特定的地方；&1是指无论标准输出在哪里