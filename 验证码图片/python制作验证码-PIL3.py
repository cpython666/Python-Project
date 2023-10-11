from PIL import Image, ImageDraw, ImageFont
import random
import string

# 随机生成n个字符
n = 6  # 设置字符个数
letters = ''.join(random.choices(string.ascii_letters + string.digits, k=n))

# 创建一个新的图片
font_size = 40
padding = 10  # 填充大小

# 获取字体的宽度和高度
font = ImageFont.truetype('arial.ttf', font_size)
text_width, text_height = font.getsize(letters)

# 计算图片宽度和高度
width = text_width + 2 * padding
height = text_height + 2 * padding

# 创建一个新的图片
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建一个画笔对象
draw = ImageDraw.Draw(image)

# 随机添加一些干扰线
for i in range(n):
    x1 = random.randint(0, width // 3)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width - width // 5)
    y2 = random.randint(0, height)
    draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=1)

# 在画布上随机绘制字母
x = padding
y = padding

for i in range(n):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    angle = random.randint(-30, 30)
    draw.text((x, y), letters[i], font=font, fill=color)

    x += text_width // n  # 水平间距可以根据字符数量平均分配

# 保存图片
image.save('captcha.png')
# 显示图片
image.show()