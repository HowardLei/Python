"""
分支结构与循环结构
注意：分支结构中，有 if 分支，其中，在 if 分支当中，不会出现 else 悬挂的情况。因为 Python 是按
     照严格的所进执行的。
     循环结构中，与 C 语言类似。while 循环的结构与 C 语言相似，for 循环均为 for in 循环，
     及遍历列表里面的数据。不能单独遍历数值。如果遍历数值的话，只能使用 while 循环。
     如果想实现之前 C 语言的 for 循环，需要调用 range() 函数。其中里面有 3 个参数，第一个参数
     为首元素的值，第二个参数为结束的值，第三个参数为每次增加的值
"""


# 1、 1 个简单的例子，输入一个成绩，将其按照成绩分别转化为 A、B、C、D
def demo1():
    score = int(input("请输入一个成绩"))
    if 100 >= score >= 90:
        print("A")
    elif 90 > score >= 80:
        print("B")
    elif 80 > score >= 60:
        print("C")
    elif score < 0 or score > 100:
        print("输入错误")
    else:
        print("D")


# 2、条件表达式（三目操作符）举例，比较两个数之间更小的数，如果写成复杂的 if 分支，如下
def demo2():
    x = int(input("请输入一个数"))
    y = int(input("请再输入一个数"))
    if x < y:
        print("两个数之间更小的是" + str(x))
    elif x > y:
        print("两个数之间更小的是" + str(y))
    else:
        print("两个数一样大")


# 上面判断函数的简单方法：取值的时候直接在里面进行 if 判断，如果是满足什么条件是什么值，如果不是则
#                    是什么值
def demo3():
    x = int(input("请输入一个数"))
    y = int(input("请在再输入另外一个数"))
    small = x if x < y else y
    print("两个数之间的最小的数为" + str(small))


# 3、一般的 for 循环。
def demo4():
    for i in range(1, 4, 2):
        print(i)
    # 上面的代码用 C 语言写法为
    # for (int i = 1; i < 4; i += 2) {
    #     printf("%d\n", i);
    # }
    # 注意：在 Python 中，range() 函数返回的一个范围对象，在 for in 循环中遍历这个对象里面的
    #      各个元素，而不是像 C 语言那样，数值是根据变量的值变化而变化。这个需要注意！！！


# 4、一般的 for in 循环
def demo5():
    name = "王尼玛"
    for element in name:
        print(element)


# 5、有关 break 的例子
def demo6():
    bingo = "我是帅哥"
    answer = input("请输入我最想听到的话")
    while True:
        if answer == bingo:
            print("输入正确")
            break
        answer = input("输入错误，请重新输入")
    print("谢谢夸奖")

# 6、关于 continue 的例子
def demo7():
    for i in range(10):
        if i % 2 != 0:
            print(i)
            continue
        i += 2 # 这个只是将 i 的值加 2 ，并不印象循环内部的值。
        print(i)

def demo8():
    for i in range(10):
        print("%d"% i)


# demo1()
# demo2()
# demo3()
# demo4()
# demo5()
# demo6()
# demo7()
demo8()