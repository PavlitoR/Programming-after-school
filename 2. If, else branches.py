def main():
    task_1()    # Ответ: True
    task_2()    # Ответ: False
    task_3()    # Ответ: 5
    task_4()    # Ответ: 30
    task_5()    # Ответ: True
    task_6()    # Ответ: Вырожденный
    task_7()    # Ответ: 7

def task_1():
    x = int(input())
    y = int(input())
    if x >= 5 and y < 25:
        print('True')
    else:
        print('False')

def task_2():
    password = input()
    password_confirmation = input()
    if password == password_confirmation:
        print('True')
    else:
        print('False')

def task_3():
    min_number = 99999999999   # Интересно, есть ли какой-нибудь минимальный/максимальный числовой объект в Python?
    for i in range(4):
        number = int(input())
        if number < min_number:
            min_number = number
    print(min_number)

def task_4():
    max_number = -99999999999
    for i in range(4):
        number = int(input())
        if number > max_number:
            max_number = number
    print(max_number)

def triangle_generator():
    triangle = [int(input()) for i in range(3)]
    return sorted(triangle)

def check_for_triangle_existence(array):
    if array[0] + array[1] >= array[2]:
        return 'True'
    else:
        return 'False'

def task_5():
    triangle = triangle_generator()
    print(check_for_triangle_existence(triangle))

def task_6():
    triangle = triangle_generator()
    if check_for_triangle_existence(triangle) == 'True':
        if triangle[0] == triangle[2]:
            print('This triangle is equilateral')
        elif triangle[0] == triangle[1] or triangle[1] == triangle[2]:
            print('This triangle is isosceles')
        elif triangle[0] + triangle[1] == triangle[2]:
            print('This triangle is degenerate')
        else:
            print('This triangle is versatile')
    else:
        print('This triangle does not exists')

def task_7():
    array = [int(input()) for i in range(4)]
    first_segment = [i for i in range(array[0], array[1] + 1)]
    second_segment = [i for i in range(array[2], array[3] + 1)]
    count = 0
    for i in first_segment:
        for g in second_segment:
            if i == g:
                count += 1
                break
    print(count)

if __name__ == "__main__":
    main()