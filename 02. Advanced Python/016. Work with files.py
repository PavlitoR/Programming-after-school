def main():
    # file_to_string_sep_by_space()
    print(string_without_marks('ППШ - лучший курс по программированию?!'))
    # file_to_dict()


def file_to_string(file_name):  # 1
    with open(file_name, 'r') as file:
        string = file.read()
    return string


def first_string_in_file(file_name):  # 2
    with open(file_name, 'r') as file:
        string = file.readline()
    return string


def file_to_array(file_name):  # 3
    with open(file_name, 'r') as file:
        array = file.readlines()
    return array


def file_to_array_without_shift(file_name):  # 4
    with open(file_name, 'r') as file:
        array = file.read()
    return array


def print_all_lines(file_name):  # 5
    with open(file_name, 'r') as file:
        for line in file:
            print(line, end='')
    return ''


def file_to_string_sep_by_space(file_name):  # 6
    string = ''
    with open(file_name, 'r') as file:
        for line in file:
            string += line.rstrip('\n') + ' '
    return string


def string_without_trash(string):  # 7
    return string.rstrip("\n\t")


def string_without_marks(string):  # 8
    return string.rstrip("?!.")


def writer(file_name, string):  # 9
    with open(file_name, 'w') as file:
        file.write(string)


def writer_with_shift(file_name, string):  # 10
    with open(file_name, 'w') as file:
        file.write(string + '\n')


def writer_from_array(file_name, array):  # 11
    with open(file_name, 'w') as file:
        file.writelines(array)


def copy_file(read_file_name, write_file_name):  # 12
    with open(read_file_name, 'r') as first_file, open(write_file_name, 'w') as second_file:
        for line in first_file:
            print(line.rstrip('\n'), file=second_file)


def copy_file_with_features(read_file_name, write_file_name):  # 13
    with open(read_file_name, 'r') as first_file, open(write_file_name, 'w') as second_file:
        for line in first_file:
            if line.startswith('hello') and line.rstrip("\n").endswith('world'):
                second_file.write(line)


def file_to_dict(file_name):  # 14
    dictionary = dict()
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            array = line.split()
            if array[2].isdigit():
                name, pet, pet_age = array[0], array[1], array[2]
                dictionary[name] = (pet, pet_age)
        return dictionary


if __name__ == '__main__':
    main()
