# -*- coding: UTF-8 -*-
import numpy as np
import torch
from torch.autograd import Variable
import one_hot_encoding
import setting
import my_dataset
from cnn_model import CNN
import os

# -------------------------------
model = 'model-84.pkl'  # 设置权重路径
# -------------------------------


def main():
    print("[*] Start to load CNN Net!")
    cnn = CNN()
    cnn.eval()
    modelPath = os.path.join(setting.CURRENT_PATH, 'result', model)
    # 判断是否存在GPU
    if not torch.cuda.is_available():
        cnn.load_state_dict(torch.load(modelPath, map_location='cpu'))
        print('[*] CPU In Use!')
    else:
        cnn.load_state_dict(torch.load(modelPath))
        print('[*] GPU In Use!')
    # 开始初始化数据集
    print("[*] Start to load dataSet!")

    predict_dataloader = my_dataset.get_predict_data_loader()

    for i, (images, labels) in enumerate(predict_dataloader):
        image = images
        vImage = Variable(image)
        predict_label = cnn(vImage)
        predict = ''
        for x in range(setting.MAX_CAPTCHA):
            predict += setting.ALL_CHAR_SET[
                np.argmax(
                    predict_label[0, x * setting.ALL_CHAR_SET_LEN:(x + 1) * setting.ALL_CHAR_SET_LEN].data.numpy())
            ]
        true_label = one_hot_encoding.decode(labels.numpy()[0])
        if predict == true_label:
            print(f'[✓] the predict: {predict} == the true : {true_label}')
        else:
            print(f'[x] the predict: {predict} != the true : {true_label}')


if __name__ == '__main__':
    main()