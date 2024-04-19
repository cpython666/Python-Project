# -*- coding: utf-8 -*-
# @Time    : 2023/10/10 11:25
# @QQ  : 2942581284
# @File    : 字符画.py
from PIL import Image
# 字符集，您可以根据需要进行修改
# ASCII_CHARS = "@#+=-"
ASCII_CHARS='@%#*+=-:. '
# 将灰度值映射到字符
def scale_gray(value):
    scale = (len(ASCII_CHARS) - 1) / 255
    return ASCII_CHARS[int(value * scale)]
# 将图像转换为字符画
def image_to_ascii(image_path, output_width=100):
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio)
    resized_image = image.resize((output_width, new_height))
    grayscale_image = resized_image.convert('L')  # 转换为灰度图像
    # 将灰度图像转换为NumPy数组
    # import numpy as np
    # grayscale_matrix = np.array(grayscale_image)
    # 打印灰度矩阵
    # print(grayscale_matrix)
    ascii_art = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Character Pattern</title>
                </head>
                <body>
                <pre id="a">
                """
    for y in range(new_height):
        for x in range(output_width):
            pixel_value = grayscale_image.getpixel((x, y))
            ascii_art += scale_gray(pixel_value)
        ascii_art += "\n"
    ascii_art+='''
            </pre>
            </body>
            <script>
                // 获取字符图案元素
                const characterPattern = document.getElementById("a");
                const characters = "@%#";
                function randomizePattern() {
                  // 将字符图案文本分割为单个字符
                  const patternText = characterPattern.textContent.trim();
                  const patternCharacters = patternText.split("");
                  // 替换非空格字符为随机字符
                  for (let i = 0; i < patternCharacters.length; i++) {
                    // if (patternCharacters[i] !== ' ' && patternCharacters[i] !== '\\n') {
                        if (patternCharacters[i] == '@' || patternCharacters[i] == '%' || patternCharacters[i] == '#') {
                      const randomCharacter = characters[Math.floor(Math.random() * characters.length)];
                      patternCharacters[i] = randomCharacter;
                    }
                  }
                  // 更新字符图案文本
                  characterPattern.textContent = patternCharacters.join("");
                }
                // 定期调用 randomizePattern 函数以创建动画效果
                setInterval(randomizePattern, 300); // 每100毫秒替换一次字符
              </script>
            </html>'''

    return ascii_art

if __name__ == "__main__":
    input_image_path = "派森斗罗.png"  # 替换为您自己的图像文件路径
    # input_image_path = "pattern_with_padding.png"  # 替换为您自己的图像文件路径
    output_width = 200  # 输出字符画的宽度
    ascii_art = image_to_ascii(input_image_path, output_width)
    print(ascii_art)
    with open(input_image_path+'.html','w',encoding='utf-8') as f:
        f.write(ascii_art)