from PIL import Image, ImageDraw
import math
# 指定图片的初始内半径和外半径，圆层数，内外半径增加步长，
INNER_RADIUS = 80
OUTER_RADIUS = 140
radius_step=50
# 图片初始数量及其增加步长
n = 4
n_step=3
# 层数
x=5
# 创建一个新的图像，用于排列图片
image_size=(OUTER_RADIUS+radius_step*(x-1)) * 2
result_image = Image.new('RGBA', (image_size, image_size), (0, 0, 0, 0))
# 创建一个绘图对象
draw = ImageDraw.Draw(result_image)
for i in range(x):
    # 循环处理每个图片
    inner_radius = INNER_RADIUS+i*radius_step
    outer_radius = OUTER_RADIUS+i*radius_step
    print(f'第{i+1}层，内圈半径为：{inner_radius},外圈半径为{outer_radius}')
    n_tmp=n+n_step*i
    for j in range(n_tmp):
        # 计算每个图片的角度
        angle = ((360 / n_tmp) * j + 30*i)%360
        # 计算每个图片的位置坐标
        inner_x = int(image_size//2 + inner_radius * math.sin(math.radians(angle)))
        # inner_x = int( (INNER_RADIUS+radius_step*x) + inner_radius * math.sin(math.radians(angle))*(i+1))
        inner_y = int( image_size//2 - inner_radius * math.cos(math.radians(angle)))
        # inner_y = int( (INNER_RADIUS+radius_step*x) - inner_radius * math.cos(math.radians(angle))*(i+1))
        if j==0:
            print(inner_x,inner_y)
        # 打开图片文件或创建一个新图像
        sub_image = Image.open(r'D:\python_pycharm\test\蚊香图\frames_\cropped_frame_05520.png')  # 在这里创建一个新图像，或者打开你的图片文件
        sub_image=sub_image.convert('RGBA')
        sub_image=sub_image.resize((100,60),resample=Image.BICUBIC)
        # sub_image = Image.new('RGB', (100, 30), (0, 0, 0))  # 在这里创建一个新图像，或者打开你的图片文件
        # 计算旋转角度以确保图片朝向圆心
        rotation_angle = -angle
        # 旋转图片
        sub_image = sub_image.rotate(rotation_angle, resample=Image.BICUBIC,expand=True,fillcolor= (0, 0, 0,0),
                                     # 旋转默认图像中心，这行代码可不选，一样
                                     center=(sub_image.width // 2, sub_image.height // 2))
        # 将子图像粘贴到结果图像上
        result_image.alpha_composite(sub_image, (inner_x - sub_image.width // 2, inner_y - sub_image.height // 2))
        # result_image.paste(sub_image, (inner_x - sub_image.width // 2, inner_y - sub_image.height // 2))
        # break

# 保存排列后的图像
result_image.save('result_image.png',format='PNG')
# 显示排列后的图像
result_image.show()
