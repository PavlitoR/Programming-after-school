import copy
import sys

def main():
    task_1()    # Ответ: 108
    task_2()    # Ответ: 5 35
    task_3()    # Ответ: 966
    task_4()    # Ответ: 32 206 137 41
    task_5()    # Ответ: 6 18 (?)
    task_6()    # Ответ: tomatoes pepper

def task_1():
    r = [45, 84, 10, 58]
    a = r
    r[0] = 54
    print(a[0] + r[0])

def task_2():
    array = [int(input()) for i in range(5)]
    array_slice = array[:]
    array_copy = array.copy()
    copy_array = copy.copy(array)
    deepcopy_array = copy.deepcopy(array)
    list_array = list(array)

    print(array_slice, array_copy, copy_array, deepcopy_array, list_array)
    print('5', sum(array))

def task_3():
    ar = [[90, 99, 109, 119]] * 4
    ar[0][0], ar[3][3] = 890, 76
    print(ar[1][0] + ar[2][3])

def task_4():
    animals = ['cat', 'cat', 'dog', 'dog', 'bird', 'capybara', 'capybara', 'capybara']
    a = dict()
    for animal in animals:
        if animal not in a:
            a[animal] = 1
        elif animal in a:
            a[animal] += 1

    ref_sum = 0
    for animal in a:
        ref_sum += sys.getrefcount(animal)
    print(ref_sum, sys.getrefcount(1), sys.getrefcount(2), sys.getrefcount(3))

def task_5():   # Ответ не сходится, не понимаю почему, вроде алгоритм работает как и было задумано
    backpack = ['capybara', 'capybara', 'capyba', 'capyba', 'capybara', 2999, 2999, 'capybara',
                [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7]] + [[8, 8]] * 5
    ref_count = 0
    is_count = 0
    for i in range(len(backpack)):
        for g in range(len(backpack)):
            if i < g:
                if backpack[i] is backpack[g]:
                    # print(f'{backpack[i]} is {backpack[g]}')
                    is_count += 1
                elif backpack[i] == backpack[g]:
                    # print(f'{backpack[i]} ref {backpack[g]}')
                    ref_count += 1
    print(ref_count, is_count)

def task_6():
    recursive_salad_cesar = ['lettuce', 'chicken', 'cheese', 'sauce', 'tomatoes', 'croutons']
    recursive_salad_cesar.append(recursive_salad_cesar)
    recursive_salad_cesar[6].append('salt')
    recursive_salad_cesar[6].append('pepper')
    print(recursive_salad_cesar[4], recursive_salad_cesar[-1])

if __name__ == '__main__':
    main()