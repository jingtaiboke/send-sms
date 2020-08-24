#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取值，从0到3，取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
print('L[0:3] =', L[0:3])
# 取值前3个元素
print('L[:3] =', L[:3])

# 取值
print('L[1:3] =', L[1:3])
# 取值，取最后两个元素
print('L[-2:] =', L[-2:])
# 取值，取最后一个元素
print('L[-1]=', L[-1])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])

c = [1, 2, 3, 4, 5]
# 只写[:]就可以原样复制一个li
d = c[:]
print(d)

# tuple进行切片

a_tuple = (1, 3, 4, 5, 6, 8)
print(a_tuple[-1])

# Str 进行切片
a_str = 'Love'

print(a_str[-1])


def aaas(s):
    a_len = len(s)
    if s[0] == ' ':
        return s[1:a_len]
    elif s[-1] == ' ':
        return s[:(a_len - 2)]
    elif s[0] == ' ' and s[-1] == ' ':
        return s[1: (a_len - 2)]


if __name__ == '__main__':
    a = 'sdad '
    c = aaas(a)
    print(c)
