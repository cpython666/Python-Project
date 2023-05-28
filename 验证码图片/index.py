from PIL import Image, ImageDraw, ImageFont
import random
import string

# 设置验证码图片的宽度、高度和随机字符的个数
width, height, n = 200, 50, 4

# 随机生成n个字符
letters = ''.join(random.choices(string.ascii_letters + string.digits, k=n))

# 创建一个新的图片
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建一个画笔对象
draw = ImageDraw.Draw(image)

# 设置字体大小
font_size = int(height * 0.7)

# 从系统中选择一个合适的字体
# font = ImageFont.truetype('ITCBLKAD.TTF', font_size)
font = ImageFont.truetype('arial.ttf', font_size)

# 在画布上随机绘制字母
for i in range(n):
    color=random.randint(0,155)
    x = int(width / (n + 1)) * (i + 1)
    y = random.randint(int(height * 0.1), int(height * 0.2))
    draw.text((x, y), letters[i], font=font, fill=(color, color, color))

# 随机添加一些干扰线
for i in range(n):
    x1 = random.randint(0, width//3)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width-width//5)
    y2 = random.randint(0, height)
    draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=1)

# 保存图片
image.save('captcha.png')

# 显示图片
image.show()