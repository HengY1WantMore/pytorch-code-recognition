# -*- coding: UTF-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import time
import setting
import os
from tqdm import tqdm


# 随机生成字母
def random_captcha():
    oneText = []
    for _ in range(setting.MAX_CAPTCHA):
        c = random.choice(setting.ALL_CHAR_SET)
        oneText.append(c)
    return ''.join(oneText)


# 生成字符对应的验证码
def gen_text_and_image():
    image = ImageCaptcha()
    text = random_captcha()
    image = Image.open(image.generate(text))
    return text, image


if __name__ == '__main__':
    # -----------------------
    # 在这里开始设置参数
    count = 2000  # 这里设置想生成多少张图片
    path = setting.TRAIN_DATASET_PATH  # 可以选择参数 TRAIN_DATASET_PATH TEST_DATASET_PATH PREDICT_DATASET_PATH
    # -----------------------

    # 开始运行
    if not os.path.exists(path):
        print('[*] Ops! The Dir Do Not Exist!')
        os.makedirs(path)
    print('[*] The ImageMake Mission Start!')
    for i in tqdm(range(count)):
        now = str(int(time.time()))
        text, image = gen_text_and_image()
        filename = text + '_' + now + '.png'
        image.save(path + os.path.sep + filename)
    print(f'[*] The ImageMake Mission Done! See in {path}.')
