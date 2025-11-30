import time
import random
from src.sorts import bucket_sort


def timeit_once(func, *args, **kwargs) -> float:
    """
    Замеряет время работы одной функции
    :param func: функция
    :param args: позиционные аргументы
    :param kwargs: именованные аргументы
    :return: время работы функции
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def benchmark_sorts(
    arrays: dict[str, list], algos: dict[str, callable]
) -> dict[str, dict[str, float]]:
    """
    Создает словарь, в котором демонстрируется время работы сортировок на разных массивах чисел
    :param arrays: словарь из названий массивов чисел и самих массивов
    :param algos: словарь из названий функций и функций
    :return: словарь из названий массивов, названий сортировок с временем работы каждой сортировки на этом массиве чисел
    """
    dictionary = {}
    for name, arr in arrays.items():
        dictionary[name] = {}
        for title, func in algos.items():
            if func == bucket_sort:
                arr1 = [random.random() for _ in range(len(arr))]
            else:
                arr1 = list(arr)
            dictionary[name][title] = timeit_once(func, arr1)
    return dictionary
