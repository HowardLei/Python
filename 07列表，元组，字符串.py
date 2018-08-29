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
    # encode(encoding='编码格式', errors='错误的处理方法，默认为strx`ict')
    name.encode(encoding='utf-8', errors='strict')
    # 7、将字符串中 \t 转换为空格。调用 expandtabs()，默认的 tabsize=8（即空格数转换为 8），
    newWord = "wangnima\tis\ta\tbitch."
    newWord.expandtabs(tabsize=1)
    print(newWord)
    # 8、将字符串中的部分字符串替换成新的字符串。调用 replace 方法。返回新字符串。
    # replace(旧字符串, 新字符串[, count=替换次数（如果里面有多个相同的旧字符串，则可以指定最多替换几次）])
    newWord = newWord.replace("wangnima", "Benz")
    print(newWord)
    # 9、将字符串中的所有大写转化成小写/小写转换成大写。调用 lower/upper 方法。
    lowerStr = newWord.lower()
    upperStr = newWord.upper()
    print(lowerStr, upperStr)
    # 10、字符串的拼接。用 join 方法。因为如果使用 + 号进行拼接字符串，效率会变的低下。
    # 如何使用：分隔符的字符串.join(需要插入到的字符串的区间，如a果只有一个字符串，则会在这个字
    # 符串之间添加分隔的字符串，如果添加多个字符串，需要将其转换成列表来使用)
    space = ' '
    newName = space.join(name)
    print(newName)
    print(" ".join(["I", "love", "MelodyBaby."]))


# 4、字符串的 format 方法
def demo4():
    """
    在字符串的格式化方法中，有以下几种参数：位置参数、关键字参数、格式化参数
    """
    # 1、位置参数。即将字符串中添加大括号并标注数字（从 0 开始，多个参数依次填写）。然后在 format
    #            方法中依次添加里面的参数值。
    name = "{0}".format("王尼玛")
    age = 18
    weight = "{0}.{1}".format(60, 2)
    print(name, weight)
    # 2、关键字参数：即将字符串中添加大括号，并标注里面应该填写的项目，在 format 方法后赋值
    info = "我叫{name},今年{age}岁，重{weight}千克".format(name=name, age=age,
                                                  weight=weight)
    print(info)
    # 3、格式化参数方法，与 C 语言中的格式化输出类似，又有一些区别。
    """
    C 语言中，格式化输出为：printf("格式化符号……", 参数……)
    Python ：单参数：print("格式化符号" % 单参数)
             多参数：print("格式化符号……" % (参数1, 参数2, ……))
    """
    news = "今天本市发生了一件重大枪击案，一名%d岁的学生被%s用枪当场打死。" % (age, name)
    print(news)


# 5、序列
def demo5():
    # 由于列表，元组，字符串之间都有共同点。所以这些数据统称序列，有一些共同的方法。
    # 1、list 方法：如果不写参数，则创建一个空列表。如果里面有参数，则将参数里面的每个元素迭代
    #              出来，形成列表
    a = list()
    b = list(("wangnima", "zhaosanfen", "lisi"))
    # 2、tuple 方法：将序列转换成元组，使用方法与 list 相同
    c = tuple("Wangnima")
    # 3、str 方法：将数据转换成字符串
    # 4、len 方法：返回参数的长度
    d = len(c)
    # 5、max 方法：返回序列中最大的值或者是(推测：按ASCII码的顺序，返回这个码的最大值所对应的字符）
    maxElement = max(c)
    print(maxElement)
    # 6、min 方法：返回序列中最小的值或者是(推测：按ASCII码的顺序，返回这个码的最小值所对应的字符)
    minElement = min(c)
    print(minElement)
    """
    上边的两个方法必须是比较相同的数据类型。否则会报错。
    listA = [123, 4546, 341]
    listA.append("王尼玛")
    max(listA)
    这段代码实现起来会报错，报错原因如下：'>' not supported between instances of 'str' and 'int'
    """
    # 7、sum 方法：返回序偶的里面的和。注意：这里面的数据不能是非数字。
    list1 = (12, 23, 43, 22, 1, 27)
    print(sum(list1))
    # 8、sorted 方法。用来正序排序序列
    alreadyList = list(sorted(list1))
    print(alreadyList)
    # 9、reversed 方法，用来将序列中的元素逆序排列。注意：他返回的是迭代器对象。并不是列表。
    list2 = list(reversed(alreadyList))
    print(list2)
    # 10、enumerate 方法。用来枚举每个序列中的元素，形成一个新元组，第一个值为索引值，第二个值为对应索引值的元素
    list3 = list(enumerate(alreadyList))
    for e in list3:
        print(e)
    # 11、zip 方法。用来包装两个序列，返回一个新的 zip 对象，对象中有 a 数组与 b 数组的结合
    for num in range(len(alreadyList)):
        a.append(num)
    list4 = list(zip(a, alreadyList))
    print(list4)

# MARK: 练习题
def demo6():
    # 这种创建列表的方法称为列表推导式
    list1 = [(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if
             y % 2 != 0]
    print(list1)
    # list1 的创建的完整写法如下
    list2 = list()
    for x in range(10):
        for y in range(10):
            if x % 2 == 0:
                if y % 2 != 0:
                    list2.append((x, y))
    print(list2)


demo6()
