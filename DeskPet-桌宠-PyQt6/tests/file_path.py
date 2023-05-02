import os

image_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'../src/resources/images'))
files=os.listdir(image_path)
print(files)