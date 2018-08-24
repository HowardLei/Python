"""
函数的作用域：
在 Python 中，同样也有全局变量和局部变量。
全局变量：在这个代码文件内生效。
局部变量：在单个函数范围内生效。

注意：在 Python 中，如果函数外有全局变量，函数内不能直接修改全局变量。否则会创建一个新的变量。
"""
# MARK: 函数的作用域例子
# 先创建几个全局变量
out = 20


def demo1():
    inside = 12
    out = 21
    print("out in func =", out)
    print("inside in func =", inside)

"""
这个函数用 C 相当于为：
int out = 20;
void demo1() {
    int inside = 12;
    int out = 21;
    printf("out in func = %d\n", out);
    printf("inside in func = %d\n", inside);
}
"""
demo1()
print("out in files =", out)
