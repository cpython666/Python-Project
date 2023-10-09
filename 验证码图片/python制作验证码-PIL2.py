# -*- coding: utf-8 -*-
# @Time    : 2023/10/9 16:31
# @QQ  : 2942581284
# @File    : 验证码5.py
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random,string
#获取随机4个字符组合
def getRandomChar():
    chr_all = string.ascii_letters+string.digits
    chr_4 = ''.join(random.sample(chr_all,4))
    return chr_4
#获取随机颜色
def getRandomColor(low,high):
    return (random.randint(low,high),random.randint(low,high),random.randint(low,high))
#制作验证码图片
def getPicture():
    width,height = 180,60
    #创建空白画布
    image = Image.new('RGB',(width,height),getRandomColor(20,100))
    #验证码的字体
    font = ImageFont.truetype('C:/Windows/fonts/stxinwei.ttf',40)
    #创建画笔
    draw = ImageDraw.Draw(image)
    #获取验证码
    char_4 = getRandomChar()
    print(char_4)
    #向画布上填写验证码
    for i in range(4):
        draw.text((40*i+10,0),char_4[i],font = font,fill=getRandomColor(100,200))
    #绘制干扰点
    for x in range(random.randint(200,600)):
        x = random.randint(1,width-1)
        y = random.randint(1,height-1)
        draw.point((x,y),fill=getRandomColor(50,150))
    #模糊处理
    image = image.filter(ImageFilter.BLUR)
    image.save('./%s.jpg' % char_4)
getPicture()