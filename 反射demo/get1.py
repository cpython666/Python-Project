class MyClass:
    def __init__(self):
        self.x = 42

obj = MyClass()

# 获取对象属性
print(getattr(obj, 'x'))
# 输出: 42