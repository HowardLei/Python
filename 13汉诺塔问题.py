"""
汉诺塔问题
"""
def hanoi(a, b, c, n):
    if n == 1:
        return None
    elif n >= 2:
