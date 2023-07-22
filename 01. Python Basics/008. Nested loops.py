def main():
    task_1()  # Ответ: -
    task_2()  # Ответ: 26
    task_3()  # Ответ: 220 284
    task_4()  # Ответ: 1634 8208 9474


def task_1():
    for i in range(1, 11):
        for g in range(1, 11):
            print(f'{i * g:4}', end='')
        print()


def task_2():
    l, r = int(input()), int(input())
    count = 0
    for k in range(l, r + 1):
        for x in range(l, r + 1):
            for y in range(l, r + 1):
                if x ** 2 + y ** 2 == k ** 2:
                    count += 1
    print(count)


def sum_divider(number):
    summa = 0
    for i in range(1, number):
        if number % i == 0:
            summa += i
    return summa


def task_3():
    n = int(input())
    for i in range(n):
        for g in range(n):
            if i < g:
                if i == sum_divider(g) and g == sum_divider(i):
                    print(i, g)


def sum_of_digits_in_degree(number, degree):
    summa = 0
    for figure in str(number):
        summa += int(figure) ** degree
    return summa


def task_4():
    n = int(input())
    for number in range(10 ** (n - 1), 10 ** n):
        if sum_of_digits_in_degree(number, n) == number:
            print(number, end=' ')


if __name__ == '__main__':
    main()
