def main():
    print(calculate_the_quotient('555 / 2'))  # task 1
    print(password_verification('a14', 'qw2', 'ad2', '16'))  # task 2
    print(check_result_of_olympiad('Ольга Олимпиадникова'))  # task 3
    print(check_result_of_olympiad('Олеся Олимпиадникова'))  # task 3
    extremely_impolite_function()  # task 4
    anecdote()  # task 5


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
        print(f'[{first_olympiad["name"]}]', end='  ')
        print(f'победитель  {first_olympiad["winners"][name_of_participant]}')
    except KeyError:
        print('призер')
    finally:
        print('-' * 51)

    try:
        print(f'[{second_olympiad["name"]}]', end='  ')
        print(f'победитель {second_olympiad["winners"][name_of_participant][4]}')
    except KeyError:
        print('призер')
    except IndexError:
        print('победитель  5 задача не проверена')
    finally:
        print('-' * 51)
    return ''


def extremely_impolite_function():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('Тебе это не надо (ಠ_ಠ)')
        extremely_impolite_function()


class LizardInLemonadeMug(Exception):
    pass


class BarBurntDown(Exception):
    pass


class NegativeNumberOfMugs(Exception):
    pass


class TooManyNumberOfMugs(Exception):
    pass


def anecdote():
    try:
        answer = input('Добро пожаловать, что будете заказывать?\n'
                       'Мы можем предложить Вам лимонад или ящерицу в стакане\n')
        if answer == 'ящерицу в стакане':
            raise LizardInLemonadeMug
        if answer == 'где тут туалет?':
            raise BarBurntDown
        if answer == 'лимонад':
            answer = input('Сколько Вам нужно кружек\n')
            if int(answer) == 0:
                print('Пожалуйста, вот ваши 0 кружек лимонада')
            if int(answer) == 1:
                print('Пожалуйста, с вас 10 тугриков')
            if int(answer) == 2:
                raise AssertionError
            if int(answer) > 2:
                raise TooManyNumberOfMugs
            if int(answer) < 0:
                raise NegativeNumberOfMugs
            else:  # qwerty type number of mugs
                raise ValueError
    except AssertionError:
        print('У бара сегодня кризис: не больше одной кружки в одни руки')
    except ValueError:
        print('Кажется Вам уже хватит на сегодня лимонада...')
    except LizardInLemonadeMug:
        print('Сегодня ящерицы были особенно желаемыми, поэтому они закончились')
    except NegativeNumberOfMugs:
        print('Такого количества кружек не может быть и в помине')
    except TooManyNumberOfMugs:
        print('Нам не хватит кружек для выполнения Вашего заказа')
    except BarBurntDown:
        print('Бар сгорел')


if __name__ == '__main__':
    main()
