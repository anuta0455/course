# Пример 1
def task_1(n):
    num = 1
    x = 0
    while num <= n:
        x += 1 / num
        num += 1
    return x


# Пример 2
def task_2(x, n):
    num = 1
    y = 0
    while num <= n:
        y += x / num
        num += 2
    return y


# Пример 3
def task_3(n):
    num = 1
    x = 1
    while num <= n:
        x *= (num)
        num += 1
    return x


# Пример 4
def task_4(x, n):
    ans = 1
    i = 2
    while i <= n:
        ans *= (x + i) / i
        i+=1
    return ans


# Пример 5
def task_5(x, n):
    num = 2
    ans = 0
    up = 1
    while num <= n:
        ans += x * up / num
        x += 1
        num += 2
    return ans + 1


# Пример 6
def task_6(n):
    ans = 1
    x = 2
    while x <= n:
        ans *= x
        x += 2
    return ans
