# -*- coding: utf-8 -*-
# @Time    : 2023/10/2 19:49
# @QQ  : 2942581284
# @File    : 02.剪切图像.py
import os
import cv2
# 指定包含图片的文件夹路径
ori_path = 'frames'
des_path = 'frames_'
if not os.path.exists(des_path):
    os.makedirs(des_path)
# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(ori_path)]
# 定义裁剪区域的坐标 (x, y, width, height)
crop_area = (0, 450, 1080, 600)  # 示例：从左上角(100, 100)开始裁剪，宽度200，高度200
# 循环处理每个图片文件
for image_file in image_files:
    # 拼接图片文件的完整路径
    image_path = os.path.join(ori_path, image_file)
    # 读取图片
    image = cv2.imread(image_path)
    if image is not None:
        # 裁剪图片
        x, y, w, h = crop_area
        cropped_image = image[y:y + h, x:x + w]
        # 保存裁剪后的图片
        output_file = os.path.join(des_path, f"cropped_{image_file}")
        cv2.imwrite(output_file, cropped_image)
        print(f"已保存裁剪后的图片：{output_file}")
    else:
        print(f"无法读取图片：{image_path}")