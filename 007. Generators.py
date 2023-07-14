def main():
    task_1()  # Ответ: 338350
    task_2()  # Ответ: [0, 8, 16, 24, 32]
    task_3()  # Ответ: 10
    task_4()  # Ответ: 3
    task_5()  # Ответ: 220


def task_1():
    print(sum([i ** 2 for i in range(1, 101)]))


def task_2():
    a = [i for i in range(0, 20, 2)]
    b = [x * 2 for x in a]
    c = b[::2]
    print(c)


def task_3():
    array = [i for i in range(1, 21) if i % 2 == 0]
    print(len(array))


def task_4():
    array = [i for i in [int(i) for i in input().split()][::2] if i % 2 == 0]
    print(len(array))


def task_5():
    array = [i for i in range(1, 1000) if i % 7 == 0 or i % 11 == 0]
    print(len(array))


if __name__ == '__main__':
    main()
