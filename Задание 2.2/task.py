import math
# Пример 1
def task_1(A):
    x = 0
    for i in A:
        if i > 0:
            x += i
    return x


# Пример 2
def task_2(A):
    x = 0
    for i in A:
        x += i
    y = x / len(A)
    return y


# Пример 3
def task_3(A):
    x = 0
    for i in A:
        x += i
    sred = x / len(A)

    el = 0
    for i in A:
        el += (i - sred) * (i - sred)
    quatra = math.sqrt(el / len(A))
    return quatra
