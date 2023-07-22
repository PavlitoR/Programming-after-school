def main():
    print(task_1(1, 2))  # NameError: name b is not defined
    task_2()  # UnboundLocalError: local variable 'summa' referenced before assignment
    task_3('4')  # TypeError: not all arguments converted during string formatting
    print(task_4(5))  # RecursionError: maximum recursion depth exceeded in comparison
    print(task_5('a12321a'))  # IndexError: string index out of range
    print(task_6([1, 2, 3, 4, 5]))


def task_1(a, b):
    return 18 * a * b


def task_2():
    summa = 0
    for i in range(1, 11):
        summa += i
    print('The sum is', summa)


def task_3(n):
    if int(n) % 2 == 0:
        print(n, 'is even')
    else:
        print(n, 'is odd')


def task_4(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * task_4(n - 1)


def task_5(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - (i + 1)]:
            return False
    return True


def task_6(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(1, len(lst) + 1):
            result = result * i
        return result


if __name__ == '__main__':
    main()
