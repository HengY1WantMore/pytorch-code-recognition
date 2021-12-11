# 基于CNN识别验证码(Pytorch)

##  前言

参考链接：https://github.com/dee1024/pytorch-captcha-recognition

这个学期选了**人工智能**专业课(bushi🐶)!

这就是我们小组的**期末作业**了，既然要做，那就开源搞一个能用于**实战**的。

上面的仓库太旧了，以及用户体验不是很好~~(我有啥资格嫌弃)~~

然后就**重构**了一下，以及弄了下**拓展**。

##  效果与原理

- **训练集**:

```
Training set : 100k
Test set: 1k
```

使用常用的 Python 验证码生成库 ImageCaptcha。

- **卷积神经网络**:

一个多层的卷积网络CNN,，优化了one-hot编码。

------

|     类型     | 准确率 |
| :----------: | :----: |
| 4位数字+大写 | 85.5%  |
|   正在训练   | xx.xx% |

- **某效果图**：

<img src="/Users/jj/Library/Application Support/typora-user-images/image-20211211200828095.png" alt="image-20211211200828095" style="zoom:50%;" />

##  快速开始

- **步骤一：设置**

到setting.py下设置`CHOOSE_LIST`以及`MAX_CAPTCHA`

<img src="/Users/jj/Library/Application Support/typora-user-images/image-20211211201535432.png" alt="image-20211211201535432" style="zoom:30%;" />

- **步骤二：创建属于自己的训练集**

到setting.py下设置`count`以及`path`

可以选择的参数已经在注释中了。

这里建议：

训练集的数量10k+（推荐100K的训练集）

验证集的数量1k+

```bash
$ python makeImage.py 
```



<img src="/Users/jj/Library/Application Support/typora-user-images/image-20211211201749408.png" alt="image-20211211201749408" style="zoom:30%;" />

- **步骤三：训练模型**

生成的文件会存在`./result`中

```bash
$ python train.py
```

- **步骤四：测试模型**

```bash
$ python test.py
```

- **步骤五：模型做预测**

```bash
$ python predict.py
```

## 日志与展望

- 日志📝 
  - 2021-12-11: 代码基本成型。4位数字+大写字母的争取率稳定在85%左右
  
- 展望🦅

  - 开发出Burp脚本用于爆破。
  - 开发爬虫接口用于绕过验证码限制。
  - 准确率能够来到90以上。

##  联系方式

期待您的PR以及不要脸的🙇‍♀️您的更加优秀的超参数。

我们是来自**暨南大学**某不知名小组～

**负责人**联系邮箱📮 2911567026@qq.com
