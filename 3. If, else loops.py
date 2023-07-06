def main():
    task_1()    # Ответ: x % 2 != 0 and x % 10 != 5
    task_2()    # Ответ: i 10
    task_3()    # Ответ: 768182441
    task_4()    # Ответ: 3628800

def task_1():
    x = int(input())
    while x % 2 != 0 and x % 10 != 5:
        x = int(input())

def task_2():
    for i in range(10):
        print(i)

def task_3():
    k = int(input())
    n = int(input())
    summ = 0
    while k <= n:
        if k % 2 == 1:
            summ += k
            k += 2
        else:
            k += 1
    print(summ)

def task_4():
    n = int(input())
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    print(factorial)


if __name__ == '__main__':
    main()