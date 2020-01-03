def dlina():
    for i in range(len(a)):
        for q in range(len(a[i])):
            if len(a[i]) != 1:
                continue
            else:
                return "Yes"


def maxdlin():
    max_str = 0
    max_num = 0
    for i in range(len(a)):
        for q in range(len(a[i])):
            if len(a[i]) > max_str:
                max_str = len(a[i])
                max_num = i
                maxi = max(a[max_num])

    print(max_str, maxi)



a = [
    [900, 800],
    [100, 500, 600],
    [30, 89]
]
print('Есть ли в листе строк с длиной 1', dlina())
print("Максимальное число из самой длинной строки", maxdlin())
