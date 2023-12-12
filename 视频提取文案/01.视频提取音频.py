from moviepy.editor import VideoFileClip
from os import path
# 视频文件路径
video_path = r"D:\桌面\DownKyi-1.5.9\Media\大学生们！不服就来做自媒体，挨顿毒打就舒服了！\1-《认知取决于实力》 你的实力水平，就等于认知水平！-480P 清晰-AVC.mp4"

# 创建VideoFileClip对象
video_clip = VideoFileClip(video_path)
# 提取音频
audio_clip = video_clip.audio
# 保存音频为音频文件（例如，保存为WAV文件）
output_audio_path = path.basename(video_path)

audio_clip.write_audiofile(output_audio_path, codec='mp3')