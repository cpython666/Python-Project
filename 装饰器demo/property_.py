class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def email(self):
        return f"{self.first}.{self.last}@email.com"

# 创建一个 Person 实例
person = Person("张", "三")

# 访问 fullname 属性
print(person.fullname)  # 输出：张 三

# 尝试设置 fullname 属性（只读属性，会报错）
# person.fullname = "张五"  # 报错：can't set attribute