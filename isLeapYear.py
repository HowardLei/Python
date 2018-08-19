year = input("请输入一个年份，判断其是不是闰年")
while not year.isnumeric():
    year = input("请重新输入")
test = int(year)
if (test % 4 == 0 and test % 100 != 0) or test % 400 == 0:
    print(year + "是闰年")
else:
    print(year + "不是闰年")

