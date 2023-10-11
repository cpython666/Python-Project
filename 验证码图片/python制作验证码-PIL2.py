# -*- coding: utf-8 -*-
# @Time    : 2023/10/9 16:31
# @QQ  : 2942581284
# @File    : 验证码5.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

# 获取随机字符组合
def getRandomChar():
    chr_all = string.ascii_letters + string.digits
    chr_4 = ''.join(random.sample(chr_all, 4))
    return chr_4

# 获取随机颜色
def getRandomColor(low, high):
    return (random.randint(low, high), random.randint(low, high), random.randint(low, high))

# 制作验证码图片
def getPicture():
    # 获取随机字符
    char_4 = getRandomChar()
    print(char_4)

    # 计算图片宽度和高度，以适应字符的长度
    font = ImageFont.truetype('C:/Windows/fonts/stxinwei.ttf', 40)
    text_width, text_height = font.getsize(char_4)
    width = text_width + 20  # 加一些填充
    height = text_height + 20  # 加一些填充

    # 创建空白画布
    image = Image.new('RGB', (width, height), getRandomColor(20, 100))

    # 创建画笔
    draw = ImageDraw.Draw(image)

    # 向画布上填写验证码
    draw.text((10, 10), char_4, font=font, fill=getRandomColor(100, 200))

    # 绘制干扰点
    for x in range(random.randint(200, 600)):
        x = random.randint(1, width - 1)
        y = random.randint(1, height - 1)
        draw.point((x, y), fill=getRandomColor(50, 150))

    # 模糊处理
    image = image.filter(ImageFilter.BLUR)

    image.save('./%s.jpg' % char_4)

getPicture()