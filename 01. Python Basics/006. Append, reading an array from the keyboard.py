def main():
    task_1()  # Ответ: [12, 34] 46
    task_2()  # Ответ: Программирование школы
    task_3()  # Ответ: нетипичный
    task_4()  # Ответ: 234168
    task_5()  # Ответ: cat


def task_1():
    n = int(input())
    m = int(input())
    array = [n, m]
    print(array, n + m)


def task_2():
    string = input()
    array = string.split()
    print(array[0], array[-1])


def task_3():
    string = input()
    array = string.split()
    for i in range(len(array)):
        if i == 0:
            max_string = array[i]
        elif len(array[i]) > len(max_string):
            max_string = array[i]
    print(max_string)


def task_4():
    n = int(input())
    array = [i for i in range(1, n + 1)]
    sorted_array = []
    for number in array:
        if number % 3 == 0 or number % 5 == 0:
            sorted_array.append(number)
    print(sum(sorted_array))


def task_5():
    string = input()
    array = string.split()
    dictionary = dict()
    max_value = 0
    max_key = None
    for word in array:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    print(max_key)


if __name__ == '__main__':
    main()
