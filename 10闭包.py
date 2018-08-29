"""
闭包：即内部函数引用外部变量，则内部函数称为闭包(closure)

"""


def closure_demo(x):
    """
    这个函数用来演示闭包
    :param x: 其中一个数的值
    :return: 闭包内的函数。
    """

    def func1(y):
        return x * y

    return func1


# 闭包练习题：这个例子可以提醒我们在无法通过修改全局变量对值进行修改的时候，可以通过闭包对值进行
#           修改
def funX():
    x = 5

    def funY():
        nonlocal x
        x += 1
        return x

    return funY


# 注意：这个地方，a 的值指向 funY 函数
a = funX()
# 每次调用的时候 a 这个闭包的时候，由于每次修改的都是 funX 函数的值，所以输出结果应该是 6 7 8
print(a())
print(a())
print(a())
# i = closure_demo(8)
