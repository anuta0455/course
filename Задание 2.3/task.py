# todo: replace this with an actual task
def task_1(str):
    last = str.split(" ")[-1]
    return len([x for x in last])


def task_2(str):
    mass = str.split(" ")
    for i in range(1, len(mass), 2):
        mass[i - 1], mass[i] = mass[i], mass[i - 1]
        ans = ''
    for i in range(len(mass)):
        if i != len(mass) - 1:
            mass[i] += " "
    for i in mass:
        ans += i
    return ans


def task_3(str):
    mass = str.split(" ")
    count = 0
    for i in range(1, len(mass)):
        if mass[i-1][-1].lower() == mass[i][0].lower():
            count += 1


    return count
