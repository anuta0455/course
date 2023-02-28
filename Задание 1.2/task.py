# Пример 1
import math

def task_1(a, b):
    if a > b:
        result = math.sqrt(a * b) - 3
    else:
        if a == b:
            result = math.log10(2)
        else:
            if a<b:
                result = (math.log(a**3 + 1)) / b
            #result = math.log(a ^ 3 + 1, math.e) / b
    return result



# Пример 2
def task_2(a, b):
    if a<b:
        result = math.tan(a/b)+1
    else:
        if a==b:
            result = math.tan(-1)
        else:
            if a>b:
                result = math.sqrt(a*b-5)/a
    return result


# Пример 3
def task_3(a, b):
    if a>b:
        result=math.log10(a*b)+21
    else:
        if a==b:
            result = math.tan(-5)
        else:
            if a<b:
                result = math.log(3*(a/b))+1
    return result


# Пример 4
def task_4(a, b):
    if a>b:
        result = math.sqrt(a*b-1)
    else:
        if a==b:
            result = math.log10(255)
        else:
            if a<b:
                result = (math.tan(a-5))/b
    return result


# Пример 5
def task_5(a, b):
    if a>b:
        result = math.log(a/b)+31
    elif a==b:
        result = math.tan(-25)
    elif a<b:
        result=(math.cos(a*5-1))/a
    return result


# Пример 6
def task_6(a, b):
    if a<b:
        result = math.sqrt((b/a)+1)
    elif a==b:
        result = math.sqrt(25)
    elif a>b:
        result = (math.log10((a*a*a)-5))/b
    return result
