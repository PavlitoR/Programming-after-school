def main():
    task_1()    # Ответ: [2, 2, 2]
    task_2()    # Ответ: [1, 2, 2]    Почему пустой массив не попал в список?
    task_3()    # Ответ: 4.2
    task_4()    # Ответ: 32
    task_5()    # Ответ: 6

def task_1():
    n = int(input())
    a = [0]
    for i in range(n):
        x = int(input())
        a = [i] * x
    print(a)

def task_2():
    n = int(input())
    a = []
    for i in range(n):
        a = a + [i] * i
    print(a)

def sequence_generator():
    n = int(input())
    return [int(input()) for i in range(n)]

def task_3():
    sequence = sequence_generator()
    summ = 0
    for i in sequence:
        summ += i
    arithmetic_mean = summ / len(sequence)
    print(arithmetic_mean)

def task_4():
    sequence = sequence_generator()
    m = int(input())
    print(sequence[m])

def task_5():
    sequence = sequence_generator()
    summ = 0
    for i in range(0, len(sequence), 2):
        summ += sequence[i]
    print(summ)

if __name__ == '__main__':
    main()
