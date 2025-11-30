def bubble_sort(a: list[int | float]) -> list[int | float]:
    """
    Пузырьковая сортировка
    :param a: список из целых или из дробных чисел
    :return: отсортированный по возрастанию список, переданный в качестве аргумента
    """
    if len(a) > 1:
        length = len(a)
        while True:
            count = 0
            for spin in range(1, length):
                if a[spin] < a[spin - 1]:
                    a[spin], a[spin - 1] = a[spin - 1], a[spin]
                    count += 1
            if count == 0:
                break
    return a


def quick_sort(a: list[int | float]) -> list[int | float]:
    """
    Быстрая сортировка
    :param a: список из целых или из дробных чисел
    :return: отсортированный по возрастанию список, переданный в качестве аргумента
    """
    if len(a) <= 1:
        return a
    basic_element, before_basic_element, after_basic_element = [a[len(a) // 2]], [], []
    a.pop(len(a) // 2)
    for element in a:
        if element <= basic_element[0]:
            before_basic_element.append(element)
        else:
            after_basic_element.append(element)
    return (
        quick_sort(before_basic_element)
        + basic_element
        + quick_sort(after_basic_element)
    )


def counting_sort(a: list[int]) -> list[int]:
    """
    Сортировка подсчетом
    :param a: список из целых чисел
    :return: отсортированный по возрастанию список, переданный в качестве аргумента
    """
    if len(a) <= 1:
        return a
    mn, mx = min(a), max(a)
    size = mx - mn + 1
    counts = [0] * size
    for x in a:
        counts[x - mn] += 1
    res = []
    for idx, value in enumerate(counts):
        res.extend([idx + mn] * value)
    return res


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Поразрядная сортировка
    :param a: список из целых чисел
    :param base: основание системы счисления чисел
    :return: отсортированный по возрастанию список, переданный в качестве первого аргумента
    """
    if len(a) <= 1:
        return a

    neg = [-x for x in a if x < 0]
    pos = [x for x in a if x >= 0]

    def _radix_non_negative(arr: list[int], base: int) -> list[int]:
        if not arr:
            return []
        max_val = max(arr)
        rad = 1
        while max_val // rad > 0:
            buckets = [[] for _ in range(base)]
            for num in arr:
                digit = (num // rad) % base
                buckets[digit].append(num)
            arr = [num for bucket in buckets for num in bucket]
            rad *= base
        return arr

    sorted_pos = _radix_non_negative(pos, base)
    sorted_neg_abs = _radix_non_negative(neg, base)
    sorted_neg = [-x for x in sorted_neg_abs[::-1]]
    return sorted_neg + sorted_pos


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Сортировка "вёдрами"
    :param a: список из дробных чисел из диапазона [0, 1)
    :param buckets: количество вёдер, по которым будут распределяться числа; по умолчанию количество вёдер равно None,
    если в качестве второго аргумента не передать кол-во вёдер, то в таком случае при выполнении сортировки оно приравняется к 5
    :return: отсортированный по возрастанию список, переданный в качестве аргумента
    """
    if buckets == None:
        buckets = 5
    mass_of_buckets = [[] for _ in range(buckets)]
    cur_mass = 0
    while cur_mass != len(mass_of_buckets):
        for element in a:
            if 1 / buckets * (cur_mass) <= element < 1 / buckets * (cur_mass + 1):
                mass_of_buckets[cur_mass].append(element)
        cur_mass += 1
    for _ in mass_of_buckets:
        bubble_sort(_)
    final_mass = []
    for elem in mass_of_buckets:
        final_mass.extend(elem)
    return final_mass


def heap_sort(a: list[int | float]) -> list[int | float]:
    """
    Пирамидальная сортировка
    :param a: список из целых или из дробных чисел
    :return: отсортированный по возрастанию список, переданный в качестве аргумента
    """
    if len(a) <= 1:
        return a
    last_parent = (len(a) - 2) // 2
    cur_parent = last_parent
    while cur_parent != -1:
        left_child = 2 * cur_parent + 1
        right_child = 2 * cur_parent + 2
        if len(a) <= left_child:
            cur_parent -= 1
        elif len(a) > left_child and len(a) == right_child:
            if a[cur_parent] < a[left_child]:
                a[cur_parent], a[left_child] = a[left_child], a[cur_parent]
            cur_parent -= 1
        elif len(a) > left_child and len(a) > right_child:
            pivot = cur_parent
            l, r = left_child, right_child
            while a[pivot] < max(a[l], a[r]):
                if a[l] > a[r]:
                    largest = l
                else:
                    largest = r
                a[pivot], a[largest] = a[largest], a[pivot]
                pivot = largest
                l, r = 2 * pivot + 1, 2 * pivot + 2
                if r >= len(a) or l >= len(a):
                    break
            if l < len(a) <= r:
                if a[pivot] < a[l]:
                    a[pivot], a[l] = a[l], a[pivot]
            cur_parent -= 1

    n = len(a)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]

        pivot = 0
        while True:
            left = 2 * pivot + 1
            right = 2 * pivot + 2
            largest = pivot

            if left < end and a[left] > a[largest]:
                largest = left
            if right < end and a[right] > a[largest]:
                largest = right

            if largest == pivot:
                break

            a[pivot], a[largest] = a[largest], a[pivot]
            pivot = largest

    return a
