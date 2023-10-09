from captcha.image import ImageCaptcha
# https://github.com/lepture/captcha
import random,string

chr_4 = ''.join(random.sample(string.ascii_letters + string.digits, 4))
image = ImageCaptcha().generate_image(chr_4)
image.save('./%s.jpg' % chr_4)