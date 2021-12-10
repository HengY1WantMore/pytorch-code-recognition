# -*- coding: UTF-8 -*-

import numpy
import setting

# Note: 重构独热码编码
# Time: 2021/12/7 10:29 下午
# Author: HengYi
# CHARACTER = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#              'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
#              'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
#              'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
#              'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44,
#              'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53,
#              's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61
#              }
CHARACTER = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
             'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
             'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35
             }


# 原来的独热码编码时位置计算太依赖数字，这样每次改动图片大小时都有可能对应改动编码算法。
# 而且解码也必须依赖数字。从这两个角度优化，新的独热码代码如下：
# 参考链接 https://github.com/dee1024/pytorch-captcha-recognition/issues/18
# 在此基础上进行了针对性部署，达到了相同的效果

def encode(value):
    order = []
    vector = numpy.zeros(setting.MAX_CAPTCHA * len(CHARACTER), dtype=float)
    for k, v in enumerate(value):
        index = k * len(CHARACTER) + CHARACTER.get(v)
        vector[index] = 1.0
        order.append(index)
    return vector


def decode(value) -> str:
    value = list(value.nonzero()[0])
    res = []
    for ik, iv in enumerate(value):
        val = iv - ik * len(CHARACTER) if ik else iv
        for k, v in CHARACTER.items():
            if val == int(v):
                res.append(k)
                break
    return "".join(res)


if __name__ == '__main__':
    code = '0A2J'
    vec = encode(code)
    print(vec)
    print(decode(vec))

# -*- coding: UTF-8 -*-
# import numpy as np
# import setting
#
#
# def encode(text):
#     vector = np.zeros(setting.ALL_CHAR_SET_LEN * setting.MAX_CAPTCHA, dtype=float)
#
#     def char2pos(c):
#         if c == '_':
#             k = 62
#             return k
#         k = ord(c) - 48
#         if k > 9:
#             k = ord(c) - 65 + 10
#             if k > 35:
#                 k = ord(c) - 97 + 26 + 10
#                 if k > 61:
#                     raise ValueError('error')
#         return k
#
#     for i, c in enumerate(text):
#         idx = i * setting.ALL_CHAR_SET_LEN + char2pos(c)
#         vector[idx] = 1.0
#     return vector
#
#
# def decode(vec):
#     char_pos = vec.nonzero()[0]
#     text = []
#     for i, c in enumerate(char_pos):
#         char_at_pos = i  # c/63
#         char_idx = c % setting.ALL_CHAR_SET_LEN
#         if char_idx < 10:
#             char_code = char_idx + ord('0')
#         elif char_idx < 36:
#             char_code = char_idx - 10 + ord('A')
#         elif char_idx < 62:
#             char_code = char_idx - 36 + ord('a')
#         elif char_idx == 62:
#             char_code = ord('_')
#         else:
#             raise ValueError('error')
#         text.append(chr(char_code))
#     return "".join(text)
#
#
# if __name__ == '__main__':
#     e = encode("BK7H")
#     print(decode(e))
