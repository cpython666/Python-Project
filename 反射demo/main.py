class MyClass:
    def __init__(self, x):
        self.x = x
    def my_method(self):
        print("Hello from my_method")
obj = MyClass(10)

# 使用getattr动态获取属性和方法
print(getattr(obj, 'x'))  # 输出：10
getattr(obj, 'my_method')()  # 输出：Hello from my_method

# 使用hasattr检查属性是否存在
print(hasattr(obj, 'x'))  # 输出：True
print(hasattr(obj, 'y'))  # 输出：False

# 使用setattr动态设置属性
setattr(obj, 'y', 20)
print(obj.y)  # 输出：20

# 使用delattr动态删除属性
delattr(obj, 'x')
print(hasattr(obj, 'x'))  # 输出：False