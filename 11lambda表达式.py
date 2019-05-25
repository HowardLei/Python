"""
lambda 函数：匿名函数。这个函数可以省去定义函数名的时间
如何创建：lambda 参数: 返回值
"""
from typing import re

t = lambda x, y: 2 * x + y
# print(t(2, 3))

# 有关 lambda 函数的补充 BIF
# 1、filter(函数或 None, 迭代器) 函数：过滤器函数。前面的函数表示过滤规则返回一个过滤器对象。
# 如果满足这个过滤规则，则保留下来，如果不满足，则将其筛选出来。
p = filter(lambda x: x % 2, range(100))
for e in list(p):
    print(e)

# 2、映射函数 map(映射函数，定义域)。返回一个迭代器。
g = map(lambda x: 2 * x, range(10))
print(tuple(g))
t = lambda x, y=3: x * y

def func(x):
    if x % 2:
        return x
    else:
        return None


p = filter(lambda x: not x % 3, range(100))
# 注意：filter 函数可以与列表推导式互相转化，上行的函数可以用下行的推导式等价完成。
list1 = [x for x in range(100) if x % 3 == 0]
print(list1)
# 将 zip 函数中打包的元组转换成列表
tuple_q = zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(tuple_q))
# 转换成列表的代码
list_q = list(map(lambda x: x + 1, range(1, 10, 2)))
list_s = list(range(1, 10, 2))
list_all = list()
num = 0
for e in list_q:
    list_all.append([list_s[num], e])
    num += 1
    num += 2
print(list_all)
# 上面的代码简化代码为
list_all = list(map(lambda x, y: [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print(list_all)