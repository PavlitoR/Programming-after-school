def main():
    print(sum_array([1, 7, 42, 12, 10, 1, 4, 0]))  # Ответ: 77
    print(check_range_for_number(7, [1, 9]))  # Ответ: True
    print(check_for_perfection(8128))  # Ответ: True
    print(check_for_palindrome(1234567899876554321))  # Ответ: False
    print(check_for_simplicity(123321))  # Ответ: False
    print(fibonacci_number(10))  # Ответ: 34


def sum_array(array):
    summa = 0
    for number in array:
        summa += number
    return summa


def check_range_for_number(number, array):
    flag = False
    for i in range(array[0], array[-1] + 1):
        if i == number:
            flag = True
    return flag


def sum_of_digits_in_degree(number, degree):  # Использовал эту функцию в прошлом дз
    summa = 0
    for figure in str(number):
        summa += int(figure) ** degree
    return summa


def check_for_perfection(number):
    if sum_of_digits_in_degree(number, 1) == number:
        return True
    else:
        return False


def check_for_palindrome(number):
    string_number = str(number)
    flag = True
    for i in range(len(string_number)):
        if string_number[i] != string_number[-i - 1]:
            flag = False
    return flag


def check_for_simplicity(number):
    flag = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                flag = False
    return flag


def fibonacci_number(index):
    if index == 1:
        return 0
    if index == 2:
        return 1
    if index > 2:
        return fibonacci_number(index - 1) + fibonacci_number(index - 2)


if __name__ == '__main__':
    main()
