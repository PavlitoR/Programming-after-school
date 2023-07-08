def main():
    task_1()  # Ответ: [3, 9, 15]
    task_2()  # Ответ: [10, 12, 14, 16]
    task_3()  # Ответ: 50 2500
    task_4()  # Ответ: 8 64 512 4096 32768 262144 2097152 16777216 14
    task_5()  # Ответ: 1


def task_1():
    n = int(input())
    array = []
    for i in range(n):
        if i % 3 == 0 and i % 6 != 0:
            array.append(i)
    print(array)


def task_2():
    n = int(input())
    array = []
    for i in range(10, n + 1):
        if i % 2 == 0:
            array.append(i)
    print(array)


def task_3():
    n = int(input())
    summ = 0
    if n % 2 == 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                summ += 1
    else:
        for i in range(1, n + 1):
            if i % 2 != 0:
                summ += i
    print(summ)


def task_4():
    n = int(input())
    count = 0
    if n % 3 == 0:
        m = int(input())
        for i in range(1, n + 1):
            if i % m == 0:
                count += 1
        print(count)
    else:
        for i in range(1, n + 1):
            print(n ** i, end=' ')


def task_5():
    a = int(input())
    b = int(input())
    n = int(input())
    hypotenuses = [int(input()) for i in range(n)]
    count = 0
    for hypotenuse in hypotenuses:
        if (a ** 2) + (b ** 2) == hypotenuse ** 2:
            if hypotenuse > 10 and hypotenuse % 3 == 0 or hypotenuse % 4 == 0:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
