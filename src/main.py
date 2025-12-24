from funcs import factorial, factorial_recursive, fib, fibo_recursive
from sorts import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
)
from Stack.Stack_node import Stack_node
from Stack.Staсk_list import Stack_lst
from Stack.Stack_queue import Stack_q
from Benchmarks import timeit_once, benchmark_sorts
import random


def float_numbers(numbers: str) -> bool:
    """
    Проверяет что все введённые числа - дробные
    :param numbers: строка из чисел
    :return: True or False
    """
    num = numbers.split()
    for _ in num:
        try:
            _ = float(_)
        except ValueError:
            return False
    return True


def int_numbers(numbers: str) -> bool:
    """
    Проверяет что все введённые числа - целые
    :param numbers: строка из чисел
    :return: True or False
    """
    num = numbers.split()
    for _ in num:
        try:
            _ = int(_)
        except ValueError:
            return False
    return True


def rand_int_array(n: int, left: int, right: int) -> list[int]:
    """
    Создает список из случайных целых чисел
    :param n: кол-во чисел в списке
    :param left: левая границы числового промежутка
    :param right: правая границы числового промежутка
    :return: список целых чисел
    """
    return [random.randint(left, right) for _ in range(n)]


def rand_float_array(n: int) -> list[float]:
    """
    Создает список из случайных дробных чисел из промежутка от 0 до 1
    :param n: кол-во чисел в списке
    :return: список дробных чисел из промежутка от 0 до 1
    """
    return [random.random() for _ in range(n)]


def main() -> None:
    """
    Основная функция программы, запускающая все модули
    :return: None
    """
    while True:
        try:
            n = int(input())
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print(
                "Введите число n - n-ый член последовательности Фибоначчи и n-факториал. "
            )
    print(
        factorial(n), factorial_recursive(n), fib(n), fibo_recursive(n), end="\n\n"
    )  # n-ый член последовательности Фибоначчи и факториал n
    arr1 = rand_int_array(30, -444444, 444444)
    arr2 = rand_int_array(30, -444444, 444444)
    arr3 = rand_int_array(30, -444444, 444444)
    arr4 = rand_int_array(30, -444444, 444444)
    arr5 = rand_float_array(30)
    arr6 = rand_int_array(30, -444444, 444444)
    try:
        buckets = int(input())
    except ValueError:
        print("buckets = None. ")
        buckets = None

    print(  # Время работы каждой сортировки
        "Bubble Sort: ",
        bubble_sort(arr1),
        f"time: {timeit_once(bubble_sort, arr1)}",
        "Quick Sort: ",
        quick_sort(arr2),
        f"time: {timeit_once(quick_sort, arr2)}",
        "Counting Sort: ",
        counting_sort(arr3),
        f"time: {timeit_once(counting_sort, arr3)}",
        "Radix Sort: ",
        radix_sort(arr4),
        f"time: {timeit_once(radix_sort, arr4)}",
        "Bucket Sort: ",
        bucket_sort(arr5, buckets),
        f"time: {timeit_once(bucket_sort, arr5, buckets)}",
        "Heap Sort: ",
        heap_sort(arr6),
        f"time: {timeit_once(heap_sort, arr6)}",
        sep="\n\n",
        end="\n\n",
    )

    while True:  # Тестируем три вида стека
        string = input(
            "Введите, какой стек хотите протестировать: Node Stack, List Stack или же Queue Stack? Для выхода из программы напишите quit. "
        )
        if string == "Node Stack":
            st = Stack_node()
        elif string == "List Stack":
            st = Stack_lst()
        elif string == "Queue Stack":
            st = Stack_q()
        elif string == "quit":
            break
        else:
            continue
        while True:
            command = input()
            if command == "quit":
                break
            if command == "push":
                try:
                    value = int(input())
                    st.push(value)
                except ValueError:
                    print("Для команды push введите числовое значение элемента стека. ")
            elif command == "pop":
                try:
                    print(st.pop())
                except ValueError:
                    print("Стек сейчас пустой. ")
            elif command == "peek":
                try:
                    print(st.peek())
                except ValueError:
                    print("Стек сейчас пустой. ")
            elif command == "is_empty":
                print(st.is_empty())
            elif command == "len":
                print(st.__len__())
            elif command == "min":
                try:
                    print(st.min())
                except ValueError:
                    print("Стек сейчас пустой. ")
            else:
                print(
                    "Неверная команда. Используйте команды из списка push, pop, peek, is_empty, len, min. Для выхода из тестирования стека напишите quit."
                )

    len_lst, pointer = [], 0  # Тестируем сортировки
    while True:
        try:
            count = int(input("Введите положительное количество списков с числами: "))
            if count < 1:
                continue
            break
        except ValueError:
            print("Введите одно число. ")
    new_d = {}
    while count != 0:
        name = input("Введите название списка: ")
        while name in new_d:
            name = input("Введите уникальное название списка: ")
        while True:
            numbers = input("Введите список чисел через пробел: ")
            if numbers == "не чёта не хочу" or float_numbers(numbers) == True:
                break
        if numbers == "не чёта не хочу":
            numbers = rand_float_array(random.randint(10, 44))
        else:
            numbers = [float(x) for x in numbers.split()]
        len_lst.append(len(numbers))
        count -= 1
        new_d[name] = numbers
    dictionary_alg = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Bucket Sort": bucket_sort,
        "Heap Sort": heap_sort,
    }
    for arrays, algorhythm in benchmark_sorts(new_d, dictionary_alg).items():
        print(f"{arrays}, {len_lst[pointer]}:")
        pointer += 1
        for _, __ in algorhythm.items():
            print(f"            {_}: {__}")

    #   ОТЧЁТ С БЕНЧМАРКАМИ
    point, lst = 0, []
    new_d = {}
    count_b = 4
    try:
        while count_b != 0:
            name = input("Введите уникальное название списка: ")
            while True:
                numbers = input("Введите список чисел через пробел: ")
                if numbers == "не чёта не хочу" or int_numbers(numbers) == True:
                    break
            if numbers == "не чёта не хочу":
                numbers = rand_int_array(random.randint(10, 44), -10000, 10000)
            else:
                numbers = [int(x) for x in numbers.split()]
            lst.append(len(numbers))
            count_b -= 1
            new_d[name] = numbers
        dictionary_alg = {
            "Bubble Sort": bubble_sort,
            "Quick Sort": quick_sort,
            "Counting Sort": counting_sort,
            "Radix Sort": radix_sort,
            "Heap Sort": heap_sort,
        }
        for arrays, algorhythm in benchmark_sorts(new_d, dictionary_alg).items():
            print(f"{arrays}, {lst[point]}:")
            point += 1
            for _, __ in algorhythm.items():
                print(f"            {_}: {__}")
    except MemoryError:
        print(
            "Введено слишком большое число. Компьютер не справился. Программа завершена."
        )


if __name__ == "__main__":
    main()
