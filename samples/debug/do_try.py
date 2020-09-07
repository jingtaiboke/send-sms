#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常处理：
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生

"""

# eg:1
"""
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
"""
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常")
except IOError:
    print("error 没有找见文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()


# eg2:
def temp_convert(var):
    try:
        return int(var)
    except ValueError:
        print("参数没有函数数字", var)


temp_convert("ss")



try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
