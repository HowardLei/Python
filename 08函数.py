"""
函数：组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
定义一个函数：def 关键字
def 函数名(参数名):
    代码段
    # 如果需要返回值，则在最后写 return 的值即可。否则 Python 默认写 return None
    # 如何证明返回值为 None，print（没写 return 的函数即可）

注意：在 Python 中，参数的传递是值传递，不进行类型检查。所以需要进行类型检查时，请再写检查函数。
补充：函数文档
    在 Python 中，用（“”“”“”）这种形式来写函数文档。因为在开发的时候，总会有时候忘记函数的功
    能，而函数文档就是在你不知道函数的具体功能的时候提醒的工具。更好的理解这个函数功能。
函数文档与注释的区别
    普通的注释只是在所处的行有提示作用
    函数文档可以在调用函数的时候 IDE 会自动识别并且显示提示的内容
如何打印函数文档
    函数名.__doc__（注意：函数名后面无括号）
"""


# MARK: 简单的函数的例子无任何参数的例子。
def demo1():
    print("王尼玛真的是666")


# MARK: 有参数的函数。注意：Python 中的函数的参数不像其他语言设计的那样，需要定义参数的数据类型。
# 直接传值即可。
def demo2(name):
    print(name + "大傻逼")


"""
有关函数参数的问题
1、形参与实参
    形参就是定义在函数括号里面的参数。实参就是真正代入函数的参数
2、默认参数、关键字参数、收集参数
    默认参数即在参数当中设置好默认值了。如果调用函数的时候不写参数，则按照默认参数走。
    关键字参数即解决传参的时候需要记住参数的位置，用形参名=参数即可带入参数（参数多了一般用关键
    字参数好记录）
    收集参数是针对在函数中不知道需要传入多少个参数所设计的。写法：*参数名。里面的参数整体为元组。
    注意：如果函数中既有一般参数，又有收集参数，则在传一般参数的时候，需要按照关键字参数进行添
    加。否则在传入的时候，解释器都会按照收集参数进行传递。
"""


# MARK: 默认参数的例子
def default(name="王尼玛"):
    print("%s大傻逼" % name)


# MARK: 含关键字参数以及收集参数的函数
def unknownParameters(*paras, somebody):
    for e in paras:
        print(e)
    if somebody:
        print("%s是大傻逼" % somebody)
    else:
        print("错误，没有输入参数")


# MARK: 含有函数文档的函数
def hasDoc():
    """
    No parameter, only for demo.
    """
    print("这个是含有函数文档的函数")


# MARK: 内建一个 power 函数模拟 pow 函数，并返回 x 的 y 次幂。
def power(x, y):
    # 为什么不能直接这么写，还需要写一个循环才能解决问题？
    # return x ** y
    res = 1
    for i in range(y):
        res *= x
    return res


# MARK: 求最大公约数（欧几里得算法）
def GCD(x, y):
    if x % y != 0:
        GCD(y, x % y)
        return
    print("他们两个的最大公因数为%d" % y)


# MARK: 打印所有参数的和乘以基数 3 的结果
def calc(*numParas):
    res = 0
    for e in numParas:
        res += e
        print("res + %d = %d" % (e, res))
    base = 3
    res *= base
    print("res = %d" % res)


# MARK: 接上面的函数要求，如果参数的最后一个值是 5 ，则设置基数为 5 ，基数不参与求和计算
def calc2(*numParas):
    res = 0
    base = 3
    for e in numParas:
        res += e
        print("res + %d = %d" % (e, res))
    if numParas[len(numParas) - 1] == 5:
        base = 5
        res -= base
        res *= base
    else:
        res *= base
    print("res = %d" % res)


# MARK: 寻找水仙花数
def find():
    for e in range(100, 1000, 1):
        res = 0
        for u in str(e):
            number = int(u)
            he = pow(number, 3)
            res += he
        if res == e:
            print("%d是水仙花数" % e)


"""
内嵌函数：即在函数内部嵌套另外一个函数
"""


def func1():
    print("这是 func1")
    # 注意：在函数中可以嵌套函数，这个函数的作用域为 func1 中。出了 func1 ，谁都没法调用。
    def func2():
        print("这是 func2")

    func2()

def fun(var):
    var = 1314
    print(var)
var = 520
fun(var)
print(var)

# MARK: 判断是否为回文
# 方法一：根据字符串的索引进行判断
def is_huiwen1():
    text = input("请输入一句话")
    for e in range(len(text) // 2):
        if text[e] != text[len(text) - e - 1]:
            print("不是回文联")
            return
    print("是回文联")
# 方法二：将字符串反转进行比较，看是否相同。
def is_huiwen2():
    text = input("请输入一句话")
    list1 = list(text)
    list2 = list(reversed(list1))
    # 注意：在比较的时候，必须保证他们都是列表才能进行比较。
    if list1 == list2:
        print("是回文串")
    else:
        print("不是回文串")
# is_huiwen1()
is_huiwen2()
# MARK: 函数的调用，直接在需要调用的地方调用即可。
# demo1()
# demo2("王尼玛")
# print(power(2, 3))
# GCD(21, 24)
# default(name="张三丰")
# unknownParameters(123, 435, 122, 213, somebody="王尼玛")
# var = hasDoc.__doc__
# print(var)
# calc2(12, 32, 2, 4, 5)
# find()
# func1()
