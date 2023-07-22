import time


def main():
    fibonacci_number(30)
    slow_function()


def timer(function):
    def wrapper(*args, **kwargs):
        first_point = time.time()
        result = function(*args, **kwargs)
        last_point = time.time()
        print(f'Время выполнения функции: {last_point - first_point}')
        return result

    return wrapper


def cache(function):
    dictionary = dict()

    def wrapper(*args):
        if args not in dictionary:
            result = function(*args)
            dictionary[args] = result
        else:
            result = dictionary[args]
        return result

    return wrapper


def logging(function):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a', newline='\n') as file:
            file.write(f'{function.__name__} была вызвана с аргументами: {args, kwargs}\n')
            return function(*args, **kwargs)

    return wrapper


def retry(max_attempts, delay):
    def decorator(function):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                result = function(*args, **kwargs)
                if result is not None:
                    return result
                attempts += 1
                time.sleep(delay)
            return None

        return wrapper

    return decorator


@timer
@cache
@logging
def fibonacci_number(index):
    if index == 1:
        return 0
    if index == 2:
        return 1
    if index > 2:
        return fibonacci_number(index - 1) + fibonacci_number(index - 2)


@logging
@retry(2, 0)
@timer
def slow_function():
    time.sleep(2)
    return None


if __name__ == '__main__':
    main()
