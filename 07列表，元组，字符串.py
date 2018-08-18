"""
列表：理解起来就是数组的加强版：不受数据类型限制。
元组：理解起来就是不可变的列表。一旦创建不能修改。
"""


# MARK: 列表


def demo1():
    # 1、创建一个列表、注意：这个列表可以为空
    actionList = ["eat", "dink"]
    # 2、遍历列表 for in 遍历
    for e in actionList:
        print(e)
    # 3、向列表当中添加元素
    #  1）添加单元素，调用 append 方法。参数为添加的变量。注意：这个变量只能添加一次
    actionList.append("jump")
    #  2）添加多个元素。调用 extend 方法。参数为一个列表
    actionList.extend(["play", "listenMusic"])
    #  3）添加元素到指定位置。调用 insert 方法。参数 1 为添加元素的位置，参数 2 为添加的元素/列表
    #     注意：如果是添加列表的话，是将整个列表作为一个元素添加到原对象的列表。
    actionList.insert(0, "rock")
    # 4、列表的截取。形式：[start: end] 注意：如果参数写到冒号前面，就是从参数位置开始，一直截
    #             取到这个列表的结束。如果写到冒号后边，则截取的时候从列表的第一个元素，截取到
    #             下标位置（不包含下标所代表的元素）
    actionList1 = actionList[:1]
    actionList2 = actionList.copy()
    print(actionList2)
    # print(actionList1)


# MARK: 元组
def demo2():
    # 1、创建一个元组。注意：如果创建的是元组，必须含有逗号，如果是单元素元组，则需要在元素后边再
    #    添加一个逗号。否则解释器会默认识别为其他数据类型，而非元组。
    tuple1 = ("王尼玛", "张全蛋", "死导演")
    tuple2 = tuple1[:]
    # 2、元组的添加删除
    #  1) 添加，根据定位来添加元素，如果是添加到首尾，则不需要考虑下标。如果添加到指定位置，则需要
    #     根据下标对元组进行拼接。
    tuple1 = tuple1[:1] + ("hehhe",)
    #  2) 删除元组中的单个元素，即将原元组中不需要的部分进行剪切即可。
    tuple2 = tuple2[:1] + tuple2[2:]
    #  3) 删除整个元组，del 语句。但一般不使用，因为如果对象没有变量指向，就会被自动回收。
    print(tuple2)
    del tuple2


# MARK: 字符串
def demo3():
    name = "王尼玛"
    # 1、查看字符串中的长度，调用 __len__ 方法。
    length = name.__len__()
    print(length)
    # 2、查找有无字符串及其的位置。调用 find 方法。如果有，则返回第一个字符的索引值，如果没有，
    #    则返回 -1。
    # 这个方法还有两个可选参数。一个是 start（起始字符） ，一个是 end（终止字符的位置）
    hasString = name.find("尼玛")
    print(hasString)
    # 3、查找字符串中有没有数字或者是字母，调用 isalnum 方法。如果有，返回 True, 否则返回 False
    hasAlnum = name.isalnum()
    print(hasAlnum)
    # 4、查找字符串中是否只含有字母，调用 isalpha 方法。返回值为 bool 类型。
    hasAlpha = name.isalpha()
    print(hasAlpha)
    # 5、查找字符串中是否只含有数字，调用 isnumeric 方法。
    hasNum = name.isnumeric()
    print(hasNum)
    # 6、用指定编码格式对字符串进行编码，调用 encode 方法。
    # encode(encoding='编码格式', errors='错误的处理方法，默认为strict')
    name.encode(encoding='utf-8', errors='strict')
    # 7、将字符串中 \t 转换为空格。调用 expandtabs()，默认的 tabsize = 8（即空格数转换为 8），
    newWord = "OK\t"

demo3()
