def task_1(N):
    ans = 1
    for i in range(1, N + 1):
        ans *= i
    return ans


def task_2(N):
    x = y = 1
    for i in range(2, N):
        x, y = y, x + y
    return x


def task_3(N):
    mass = [i for i in range(1, N + 1) if N % i == 0]
    return mass
