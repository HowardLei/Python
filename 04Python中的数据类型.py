#1、创建一个整数。注意：在 Python 中不分整型与长整型，他的长度不受限，最长可以到电脑虚拟内存的大小
a = 10
#2、创建一个浮点数。注意：在 Python 中，科学计数法得到的数也是浮点数。
b = 5.2
#3、创建一个字符串
c = "123.22"
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