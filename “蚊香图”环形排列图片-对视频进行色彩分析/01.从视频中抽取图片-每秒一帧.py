# -*- coding: utf-8 -*-
# @Time    : 2023/10/2 18:15
# @QQ  : 2942581284
# @File    : index.py
import os
folder_path = 'frames'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

import cv2
# 视频文件路径
video_path = '玉渊谭天蚊香图.mp4'
# 打开视频文件
cap = cv2.VideoCapture(video_path)
# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频文件")
else:
    # 获取视频帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"视频总帧数: {total_frames}")
    # 获取视频帧率
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    print(f"视频帧率: {frame_rate} fps")
    # 设置帧间隔，每秒抽取一帧
    frame_interval = frame_rate // 1  # 1秒抽取1帧
    # 循环遍历视频的每一帧并保存为图像
    frame_count = 0
    while True:
        # cap.read()读取视频的下一帧，并将其存储在frame变量中
        ret, frame = cap.read()
        if not ret:
            break
        # 每隔frame_interval帧保存一帧图像
        if frame_count % frame_interval == 0:
            image_filename = f"frame_{frame_count:05d}.png"
            cv2.imwrite( os.path.join('frames',image_filename),frame)
            print(f"保存图像: {image_filename}")

        frame_count += 1
# 释放视频捕捉对象
cap.release()