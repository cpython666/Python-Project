def my_decorator(func):
    def wrapper():
        print("有函数要执行了")
        func()
        print("有函数执行完毕了")
    return wrapper
def say_hello():
    print("Hello!")

my_decorator(say_hello)()
