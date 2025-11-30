def factorial(n: int) -> int:
    """
    Вычисляет итеративно факториал числа n
    :param n: натуральное число или 0
    :return: факториал числа n
    """
    num, result = [x for x in range(1, n + 1)], 1
    for element in num:
        result *= element
    return result


def factorial_recursive(n: int) -> int:
    """
    Вычисляет рекурсивно факториал числа n
    :param n: натуральное число n или 0
    :return: факториал числа n
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def fib(n: int) -> int:
    """
    Вычисляет итеративно n-ый член последовательности Фибоначчи
    :param n: натуральное число или 0
    :return: n-ый член последовательности Фибоначчи
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibo_recursive(n: int) -> int:
    """
    Вычисляет рекурсивно n-ый член последовательности Фибоначчи
    :param n: натуральное число или 0
    :return: n-ый член последовательности Фибоначчи
    """
    if n <= 1:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
