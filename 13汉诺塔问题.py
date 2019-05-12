# 汉诺塔问题
"""
原理：
    当这3根柱子上只有1个圆盘的时候，就可以直接将第一根柱子上的圆盘移动到第三根上
    当这3根柱子上有多余2个人圆盘的时候，就将其想象成一个柱子上
"""


def hanoi(n, x, y, z):
    if n == 1:
        print(x, "->", z)
    elif n >= 2:
        hanoi(n - 1, x, z, y)
        print(x, "->", z)
        hanoi(n - 1, y, x, z)


x = 'x'
y = 'y'
z = 'z'
hanoi(3, x, y, z)
