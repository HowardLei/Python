"""
递归：函数调用自身的行为
"""
# 阶乘（非递归版本）
from _ast import If


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


# 斐波那契数列（非递归版本）
def fibonacci_sequence(num: int):
    first = 1
    second = 1
    if num == 1 or num == 2:
        return first
    elif num > 2:
        for i in range(0, num // 2, 1):
            first += second
            second += first
        if num % 2:
            return first
        else:
            return second
    else:
        while True:
            next_num = int(input("请重新输入"))
            fibonacci_sequence(next_num)


# 斐波那契数列（递归版本）
def fibonacci_sequence_recursion(num: int):
    if num == 1 or num == 2:
        return 1
    elif num > 2:
        return fibonacci_sequence_recursion(
            num - 1) + fibonacci_sequence_recursion(num - 2)


print(lots_muitiple(6))
print(fibonacci_sequence(15))
print(fibonacci_sequence_recursion(15))
