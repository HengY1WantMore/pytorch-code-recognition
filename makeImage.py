# -*- coding: UTF-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import time
import setting
import os

def random_captcha():
    text = []
    for i in range(setting.MAX_CAPTCHA):
        c = random.choice(setting.ALL_CHAR_SET)
        text.append(c)
    return ''.join(text)

# 生成字符对应的验证码
def gen_text_and_image():
    image = ImageCaptcha()
    text = random_captcha()
    image = Image.open(image.generate(text))
    return text, image

if __name__ == '__main__':
    count = 90000
    path = setting.TRAIN_DATASET_PATH    #通过改变此处目录，以生成 训练、测试和预测用的验证码集
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(count):
        now = str(int(time.time()))
        text, image = gen_text_and_image()
        filename = text+'_'+now+'.png'
        image.save(path  + os.path.sep +  filename)
        print('saved %d : %s' % (i+1,filename))

