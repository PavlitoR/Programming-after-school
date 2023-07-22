def main():
    print(list_to_dict([1, 2, 3, 4, 5]))  # Ответ: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    create_and_print_dict(5)  # Ответ: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    multiply_and_print_dict({'data1': 375, 'data2': 567,
                             'data3': -37, 'data4': 21})  # Ответ: -165209625
    punctuation_marks_counter()  # Ответ: 12
    sign_counter("kn1mb9c7c5cv5cc9cvv7cx9sd8nm4cz2bm4k6hf9d")  # Ответ: 12456789


def list_to_dict(array):
    dictionary = dict()
    for i in array:
        dictionary[i] = i
    return dictionary


def create_and_print_dict(n):
    dictionary = dict()
    for i in range(1, n + 1):
        dictionary[i] = i ** 2
    print(dictionary)
    return dictionary


def multiply_and_print_dict(dictionary):
    creation = 1
    for number in dictionary:
        creation *= dictionary[number]
    print(creation)
    return creation


def punctuation_marks_counter():
    string = "Летний день - это день, когда наступает летнее " \
             "солнцестояние и длительность дня достигает своего максимума. В разных странах и " \
             "регионах летние дни могут иметь разную продолжительность и характеризоваться " \
             "разными погодными условиями. Вообще, летние дни обычно ассоциируются с теплой " \
             "и ясной погодой, зелеными лугами, пляжами, купанием в море или озере, пикниками и барбекю. " \
             "В летние дни люди часто отдыхают и проводят время на открытом " \
             "воздухе, занимаются спортом, путешествуют и открывают новые места!"
    count = 0
    for sign in string:
        if sign in '.,:;!?':
            count += 1
    print(count)


def sign_counter(string):
    number_dict = dict()
    letter_dict = dict()
    for sign in string:
        if sign in '0123456789':
            if sign not in number_dict:
                number_dict[sign] = 1
            else:
                number_dict[sign] += 1
        else:
            if sign not in letter_dict:
                letter_dict[sign] = 1
            else:
                letter_dict[sign] += 1

    for i in sorted(number_dict):
        print(i, end='')
    if not letter_dict:
        print('NO')


if __name__ == '__main__':
    main()
