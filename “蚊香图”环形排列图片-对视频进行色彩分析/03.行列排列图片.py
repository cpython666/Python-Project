# -*- coding: utf-8 -*-
# @Time    : 2023/10/3 1:40
# @QQ  : 2942581284
# @File    : 03.排列图片.py
from PIL import Image
import os
# 指定包含图片的文件夹路径
folder_path = 'frames_'
# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(folder_path)]
# 设置排列参数：行数和列数
rows = 20  # 行
columns = 20  # 列
# 计算每个子图像的大小
sub_image_width = 1080
sub_image_height = 600
# 创建一个新的图像，用于排列子图像
result_image = Image.new('RGB', (sub_image_width * columns, sub_image_height * rows))
# 循环处理每个图片文件
for i, image_file in enumerate(image_files):
    if i >= rows * columns:
        break  # 如果子图像数量超过指定的行列数，停止处理
    # 拼接图片文件的完整路径
    image_path = os.path.join(folder_path, image_file)
    # 打开图片
    sub_image = Image.open(image_path)
    # 调整子图像的大小，如果需要的话
    if sub_image.width != sub_image_width or sub_image.height != sub_image_height:
        sub_image = sub_image.resize((sub_image_width, sub_image_height))
    # 计算子图像在结果图像中的位置
    x = (i % columns) * sub_image_width
    y = (i // columns) * sub_image_height
    # 将子图像粘贴到结果图像上
    result_image.paste(sub_image, (x, y))
# 保存排列后的图像
result_image.save('result_image_0.png')
# 显示排列后的图像
result_image.show()
