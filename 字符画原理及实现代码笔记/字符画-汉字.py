from PIL import Image, ImageDraw, ImageFont
import numpy as np
hanzi = "编程启航"
font_size = 48
# 使用系统字体或指定字体文件
font = ImageFont.truetype("1.ttf", font_size)
# 计算汉字的大小
text_bbox = font.getbbox(hanzi)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
# 设置填充大小
padding = 20
# 创建一个空白图像，大小根据文本计算，并添加填充
pattern_size = (text_width + 2 * padding, text_height + 2 * padding)
pattern_image = Image.new('RGB', pattern_size, color=(255, 255, 255))
pattern_draw = ImageDraw.Draw(pattern_image)
# 在花纹背景上绘制汉字，考虑填充
pattern_draw.text((-text_bbox[0] + padding, -text_bbox[1] + padding), hanzi, fill=(0, 0, 0), font=font)
# 将花纹图像转换为NumPy数组以便处理
pattern_data = np.array(pattern_image)
# 在这里，您可以对花纹进行任何自定义的图像处理操作，例如添加滤镜或效果
# pass
# 创建Pillow图像对象并显示
pattern_image = Image.fromarray(pattern_data)
pattern_image.show()
# 保存花纹图像
pattern_image.save("pattern_with_padding.png")