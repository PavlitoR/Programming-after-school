def main():
    # print(calculate_the_quotient('555 / 2'))  # task 1
    # print(password_verification('a14', 'qw2', 'ad2', '16'))    # task 2
    print(check_result_of_olympiad('Ольга Олимпиадникова'))


def calculate_the_quotient(string):
    try:
        array = string.split()
        result = float(array[0]) / float(array[-1])
    except ZeroDivisionError:
        return 'ERROR'
    return result


def password_verification(*args):
    passwords = []
    for password in args:
        try:
            passwords.append(hex(int(password, 16))[2:])
        except ValueError:
            print(f'Пароль {password} не подошел')
    return passwords


def olympiad(number):
    olympiad1 = {"name": "Пробная вышка",
                 "winners": {
                     "Олеся Олимпиадникова": 594,
                     "Олег Олимпиадников": 587,
                     "Онисим Олимпиадников": 581
                 }
                 }

    olympiad2 = {"name": "Горные воробьи",
                 "winners": {
                     "Ольга Олимпиадникова": (20, 20, 19, 20),
                     "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
                     "Офелия Олимпиадникова": (20, 20, 20, 20, 13)
                 }
                 }

    if number == 1:
        return olympiad1
    elif number == 2:
        return olympiad2


def check_participant_status(name_of_participant, olympiad_results):
    for i in olympiad_results:
        if name_of_participant in olympiad_results['winners']:
            return 'победитель'
        else:
            return 'призёр'


def check_result_of_olympiad(name_of_participant):
    first_olympiad = olympiad(1)
    second_olympiad = olympiad(2)
    try:
        print(f'Имя участника: {name_of_participant}\n'
              f'[название_первой_олимпиады]  статус      балл_за_олимпиаду\n'
              f'{first_olympiad["name"]:<29}'
              f'{check_participant_status(name_of_participant, first_olympiad):<12}'
              f'{first_olympiad["winners"][name_of_participant]}\n'
              f'[название_второй_олимпиады]  статус      балл_за_пятую_задачу\n'
              f'{second_olympiad["name"]:<29}'
              f'{check_participant_status(name_of_participant, second_olympiad):<12}'
              f'{second_olympiad["winners"][name_of_participant][4]}'
              )
    except KeyError:
        print('xd')
    except IndexError:
        print('xdd')


if __name__ == '__main__':
    main()
