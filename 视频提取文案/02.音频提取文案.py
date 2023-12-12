# -*- coding: utf-8 -*-
# @Time    : 2023/10/28 19:54
# @QQ  : 2942581284
# @File    : 02.音频提取文案.py
import whisper
from os import path
model = whisper.load_model("base")
media_path=r"D:\文件夹\github_\myshare_github\Python-Project\视频提取文案\1-《认知取决于实力》 你的实力水平，就等于认知水平！-480P 清晰-AVC.mp3"
txt_name=path.basename(media_path).replace('.mp3','.txt')
result = model.transcribe(media_path)

from pprint import pprint
pprint(result)
segments=result["segments"]
text='，'.join([segment['text'] for segment in segments])

print(text)
with open(txt_name,'w',encoding='utf-8') as f:
	f.write(text)