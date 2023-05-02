from PIL import Image

# 打开 GIF 图像
gif_image = Image.open('1.gif')

# 显示 GIF 图像
# gif_image.show()

# 将图像转换为 RGBA 格式
gif_rgba = gif_image.convert('RGBA')

# 创建一个新的 RGBA 格式图像
transparent_image = Image.new('RGBA', gif_image.size, (0, 0, 0, 0))

# 将 GIF 图像中的非白色像素设置为透明
a=60
for y in range(gif_image.size[1]):
    for x in range(gif_image.size[0]):
        pixel = gif_rgba.getpixel((x, y))
        if (255 - pixel[0])>=a or (255 -pixel[1])>=a or (255-pixel[2]>=a):
            transparent_image.putpixel((x, y), pixel)

transparent_image.save('transparent_image.png', 'PNG')