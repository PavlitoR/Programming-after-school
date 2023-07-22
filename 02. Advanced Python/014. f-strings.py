def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()


def task_1():
    for name in ['Александру', 'Алексу', 'Альберту']:
        for surname in ['Вотяку', 'Вотякову', 'Вотяковичу']:
            for patronymic in ['Романовичу']:
                print(f'Диплом с отличием вручается {surname} {name} {patronymic}.')


def task_2():
    first_part = input()
    second_part = int(input())
    last_part = int(input())
    print(f'{first_part.upper()}{second_part:04}-{last_part:03}')


def task_3():
    first_number = int(input())
    last_number = int(input())
    summa = first_number + last_number
    print(f'{first_number:>9}\n{last_number:>9}\n{summa:>9}')


def task_4():
    r = int(input())
    k = int(input())
    first_amount = 100000000
    last_amount = first_amount * ((1 + r / 100) ** k)
    print(f'{last_amount:,.2f}')


def task_5():
    for a in range(1, 101):
        for b in range(1, 101):
            multiply_result = a * b
            if '0' in str(multiply_result):
                print(f'[DEBUG] {a=} {b=} {multiply_result=}')


def task_6():
    a, b, c, d = list(map(int, input().split()))
    ip = []
    for template in ['{:08b}', '{:b}', '{:o}', '{}', '{:x}']:
        ip.append('.'.join([template] * 4).format(a, b, c, d))
    for i in ip:
        print(i)


if __name__ == '__main__':
    main()
