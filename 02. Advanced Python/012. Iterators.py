def main():
    task_1()  # Ответ: 4 1 5 6
    task_2()  # Ответ: П П Ш
    task_3()  # Ответ: bee
    task_4()  # Ответ: True False (?)
    task_5()  # Ответ: 1 4 16
    task_6()  # Ответ: 1 9 25
    task_7()  # Ответ: -


def task_1():
    a = [2, 4, 6, 8]
    b = {1, 3, 5, 7}
    a_itera = iter(a)
    b_iterb = iter(b)
    next(iter(a_itera))
    print(next(iter(a_itera)), next(iter(b_iterb)))
    next(iter(b_iterb))
    print(next(iter(b_iterb)), next(iter(a_itera)))


def task_2():
    str = 'ППШ'
    iterator = iter(str)

    for x in iterator:
        print(x)


def task_3():
    d = {1: 'bee', 2: 'racoon', 3: 'snake'}
    iterator = iter(d)
    print(d[next(iterator)])


def task_4():
    a = [int(s) for s in range(1, 20)]
    iterator = iter(a)
    print(9 in iterator)
    print(9 in iterator)


def task_5():
    a = (i ** 2 for i in range(10) if i % 3 != 0)
    print(next(a))
    print(next(a))
    print(next(a))


def task_6():
    generator = (i ** 2 for i in range(1, 6))
    print(next(generator), end=' ')
    next(generator)
    print(next(generator), end=' ')
    next(generator)
    print(next(generator))


def task_7():
    stacked_deck = (f'{number} {suit}' for number in ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
                    for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades'])
    for i in range(37):
        print(next(stacked_deck))


if __name__ == '__main__':
    main()