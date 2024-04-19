class MyClass:
    def __init__(self):
        self.x = 42

obj = MyClass()

# 使用 __dict__ 获取对象的属性和方法
print(obj.__dict__)
# 输出: {'x': 42}