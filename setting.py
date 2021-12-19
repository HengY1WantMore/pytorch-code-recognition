# -*- coding: UTF-8 -*-
import os


#--------------设置参数-----------------
CHOOSE_LIST = [0, 1, 2]  # 设置要训练的集合 [NUMBER, ALPHABET, LOWER_ALPHABET] 下标
MAX_CAPTCHA = 4 # 设置验证码长度
#---------------------------------------


# 验证码中的字符
# string.digits + string.ascii_uppercase
NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
LOWER_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

ALL_SET = [NUMBER, ALPHABET, LOWER_ALPHABET]
ALL_CHAR_SET = []
for each in CHOOSE_LIST:
    ALL_CHAR_SET.append(ALL_SET[each])
ALL_CHAR_SET = sum(ALL_CHAR_SET, [])
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET)

# 设置图像
IMAGE_HEIGHT = 60 # 设置图像高度（默认不动）
IMAGE_WIDTH = 160 # 设置图像宽度（默认不动）

# 保存路径
TRAIN_DATASET_PATH = 'dataset' + os.path.sep + 'train'
TEST_DATASET_PATH = 'dataset' + os.path.sep + 'test'
PREDICT_DATASET_PATH = 'dataset' + os.path.sep + 'predict'
CURRENT_PATH = os.path.split((os.path.realpath(__file__)))[0]