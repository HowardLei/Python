"""
递归：函数调用自身的行为
"""
# 阶乘（非递归版本）
def lots_muitiple(x):
    res = 1
    while x:
        res *= x
        x -= 1
    return res
# 阶乘（递归版本）
def factorital(x):
    if x == 1:
        return 1
    else:
        return x * factorital(x - 1)
print(lots_muitiple(6))