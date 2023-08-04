def main():
    # Task 1: 231
    print(sum_even_numbers_func([14, 93, 19, 38, 18, 51, 77]))  # Task 2: [...] -> 70
    print(sum_even_numbers_imper([60, 84, 9, 49, 7, 85, 38]))   # Task 3: [...] -> 182


def sum_even_numbers_func(numbers):
    return sum(list(map(lambda x: x if x % 2 == 0 else 0, numbers)))


def sum_even_numbers_imper(numbers):    # Конструкцию функции использую как область видимости
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return sum(even_numbers)


if __name__ == "__main__":
    main()