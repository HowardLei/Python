# 1、创建一个整数。注意：在 Python 中不分整型与长整型，他的长度不受限，最长可以到电脑虚拟内存的大小
a = 10
# 2、创建一个浮点数。注意：在 Python 中，科学计数法得到的数也是浮点数。
b = 5.2
# 3、创建一个字符串
c = "123.22"
# 4、创建一个布尔类型的值，True/False 注意：True 为 1，False 为 0
d = True
e = False
# 5、如果想自己定义变量的数据类型，写法 变量名: 数据类型 = 变量值
tempStr: str = "wangnima"
string = r"c:\ProgramFiles\new"
print(string)
print(tempStr)
'''
类型转化函数
1、int()，即将其他数据类型的数据转化成 int 类型。如果这些数据不全是数，就会报错。
2、float()，即将其他数据类型的数据转化成 float 类型。如果这些数据不全是数，就会报错。
3、str()，即将其他数据类型的数据转化成 string 类型。
'''
tempInt = int(b)
tempFloat = float(a)
tempStr = str(a)
print(tempInt)
print(tempFloat)
print(tempStr)
'''
判断变量是属于那种数据类型的，用 type() 函数。判断这个数据是不是哪种数据类型，用 isinstance() 
函数来进行判断。注意；isinstance() 函数中有两个参数，第一个是变量名，第二个是数据类型。返回值为
bool 类型
'''
print(isinstance(tempStr,str))