def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()

def task_1():
    string = ''
    for i in range(3):
        word = str(input())
        string += f'{word}'
    print(string)
    return string   # Программа выведет: Программирование после школы!

def task_2():
    a = float(input())
    b = float(input())
    answer = ((2 ** 8) * (a ** 8)) - ((2 ** 4) * (a ** 4)) + ((2 ** 2) * (a ** 2)) \
            - (2 * b) + (0.5 * (b ** 0.5)) + ((a * (b ** (b + a)))/2)
    print(answer)
    return answer   # Программа выведет для a=2 и b=9: 31381124888.5

def task_3():
    a = input()
    b = input()
    print(a + b, end="!")   # Программа выведет для a=2 и b=3: 23!

def task_4():
    a = int(input())
    b = int(input())
    c = int(input())
    print('(', end='')
    print(a, b, sep=' + ', end=' - ')
    print(c, ') % 10', sep='', end=' = ')
    print((a + b - c) % 10)     # Программа выведет: (123 + 456 - 789) % 10 = 0

def task_5():
    number = int(input())
    following_number = number + 1
    previous_number = number - 1
    print(following_number, previous_number, sep='')
    return str(following_number) + str(previous_number)     # Программа выведет для 24: 2523

def task_6():
    centimeters = int(input())
    kilometers = centimeters // 100000
    print(kilometers)
    return kilometers   # Программа выведет для 123456789: 1234


if __name__ == "__main__":
    main()