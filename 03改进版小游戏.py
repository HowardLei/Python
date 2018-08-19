import random
# 与之前02里面的文件中，修改的部分如下
'''
1、在里面判断不对的时候进行提示。
2、提供多次猜数的机会
3、生成的数应该是个随机数
'''
'''
综合解决方法如下：
    1、先导入 random 模块，调用这个模块中的
'''
randomNumber = random.randint(1, 10)
temp = input("输入一个数")
while not temp.isnumeric():
    temp = input("输入格式有误，请重新输入")
guess = int(temp)
while guess != randomNumber:
    if guess > randomNumber:
        print("大了")
    else:
        print("小了")
    temp = input("请再输入一次")
    guess = int(temp)
print("回答正确")
print("游戏结束")
