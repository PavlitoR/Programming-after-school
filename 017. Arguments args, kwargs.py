def main():
    print(sum_numbers(1, 10, 100, 1000, 10000))

    print_kwargs(name='Alice', age='25', country='USA')

    strings = ['hello', 'world', 'how', 'are', 'you']
    print(filter_by_length(4, *strings))

    print(calculate_total_price(500, student='20', holiday='25'))

    custom_print(1, 2, 3, a=4, b=5, sep='-', end='!')
    custom_print('Hello', 'World', sep=' ')
    custom_print('apple', 'banana', 'cherry', sep=', ')
    custom_print(a=1, b=2, end='...')


def sum_numbers(*args):
    return sum(args)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


def filter_by_length(min_length, *args):
    filtered_array = []
    for arg in args:
        if len(arg) >= min_length:
            filtered_array.append(arg)
    return filtered_array


def calculate_total_price(price, **kwargs):
    total_discount = 0
    for discount in kwargs.values():
        total_discount += int(discount)
    return price * (1 - total_discount / 100)


def custom_print(*args, **kwargs):
    string = ''
    sep = ' '
    end = ''

    for key, value in kwargs.items():
        if key == 'sep':
            sep = value
        if key == 'end':
            end = value

    for arg in args:
        if string == '':
            string += f'{arg}'
        else:
            string += f'{sep}{arg}'

    for key, value in kwargs.items():
        if key != 'sep' and key != 'end':
            if string == '':
                string += f'{key}={value}'
            else:
                string += f'{sep}{key}={value}'

    string += f'{end}'
    print(string)


if __name__ == '__main__':
    main()
