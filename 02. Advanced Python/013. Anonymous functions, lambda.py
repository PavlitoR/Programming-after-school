from functools import reduce


def main():
    task_1()  # Ответ: Женя Вася
    task_2()  # Ответ: 8, 64, 216, 512, 1000
    task_3()  # Ответ: -1, -7, -8, -10
    task_4()  # Ответ: 40320
    task_5()  # Ответ: 6


def task_1():
    D = {'Женя': 89, 'Вася': 100, 'Марк': 71, 'Мария': 79}
    f = list(filter(lambda x: D[x] > 80, D))
    print(f)


def array_generator():
    return [int(input()) for i in range(int(input()))]


def task_2():
    array = array_generator()
    f = list(map(lambda x: x ** 3, array))
    print(f)


def task_3():
    array = array_generator()
    f = list(filter(lambda x: x < 0, array))
    print(f)


def task_4():
    array = list(range(1, int(input()) + 1))
    f = reduce(lambda x, y: x * y, array)
    print(f)


def task_5():
    array = array_generator()
    sorted_array = list(filter(lambda x: x % 3 == 0, array))
    maxim = max(sorted_array)
    print(maxim)


if __name__ == '__main__':
    main()
