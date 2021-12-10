# -*- coding: UTF-8 -*-
import numpy as np
import torch
from torch.autograd import Variable
import setting
import my_dataset
from cnn_model import CNN
import one_hot_encoding
from tqdm import tqdm

# -------------------------------
model = 'model.pkl'  # 设置权重路径
# -------------------------------


def validation(CNNModel, dataloader):
    correct = 0
    total = 0
    for i, (images, labels) in tqdm(enumerate(dataloader)):
        total += labels.size(0)  # 记录总数
        image = images
        vImage = Variable(image)
        predict_label = CNNModel(vImage)
        # 开始逐位预测(重构)
        predict = ''
        for x in range(setting.MAX_CAPTCHA):
            predict += setting.ALL_CHAR_SET[
                np.argmax(
                    predict_label[0, x * setting.ALL_CHAR_SET_LEN:(x + 1) * setting.ALL_CHAR_SET_LEN].data.numpy())
            ]
        true_label = one_hot_encoding.decode(labels.numpy()[0])
        if predict == true_label:
            correct += 1
    return correct, total


def main():
    print("[*] Start to load CNN Net!")
    cnn = CNN()
    cnn.eval()
    modelPath = 'result/' + model
    # 判断是否存在GPU
    if not torch.cuda.is_available():
        cnn.load_state_dict(torch.load(modelPath, map_location='cpu'))
        print('[*] CPU In Use!')
    else:
        cnn.load_state_dict(torch.load(modelPath))
        print('[*] GPU In Use!')
    # 开始初始化数据集
    print("[*] Start to load dataSet!")
    test_dataloader = my_dataset.get_test_data_loader()
    correctNum, totalNum = validation(cnn, test_dataloader)
    print('[*] Test Accuracy of the model on the %d test images: %f %%' % (totalNum, 100 * correctNum / totalNum))
    print('[*] The Test Mission Done.')


if __name__ == '__main__':
    main()
