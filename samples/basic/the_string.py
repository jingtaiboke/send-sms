#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
# ord(‘A’)
ord('A')
print(ord('A'))
chr(66)
print(chr(66))

# str 类型的内置函数
mystr = "Life is short，you need Python。"

print(mystr.find('short'))  # 8

# 在字符串标记的范围内查找
print(mystr.find('o', 13, 25))  # 15

print(mystr.find('hello'))  # -1

print(mystr.index('short'))

print(mystr.index('o',1,15))

