#1、在 Python 中，输入函数为input(),括号里面输入需要提示的信息，返回值为 str 类型。
temp = input("输入一个数")
#2、所以为了能够判断这个数，需要将其从 str 转换为 int 才行。
guess = int(temp)
if guess == 8:
    print("恭喜你，输入正确")
else:
    print("输入错误")
