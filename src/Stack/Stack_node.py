class Node:
    def __init__(self, value, next=None):
        """
        Инициализация объектов класса
        :param value: числовое значение элемента стека
        :param next: указатель на следующий элемент в списке
        """
        self.value = value
        self.next = next


class Stack_node:
    def __init__(self) -> None:
        """
        Инициализация объектов класса
        """
        self.top = None
        self.count = 0
        self.stack_inf = []

    def push(self, x: int) -> None:
        """
        Добавления элемента в стек
        :param x: числовое значение элемента
        :return: None
        """
        self.count += 1
        if len(self.stack_inf) == 0:
            self.stack_inf.append(x)
        else:
            self.stack_inf.append(min(x, self.stack_inf[-1]))
        new_Node = Node(x, self.top)
        self.top = new_Node

    def pop(self) -> int:
        """
        Удаление верхнего элемента в стеке
        :return: None
        """
        if self.top == None:
            raise ValueError("Стек пустой")
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        self.stack_inf.pop()
        return value

    def peek(self) -> int:
        """
        Проверка верхнего элемента в стеке
        :return: значение верхнего элемента в стеке
        """
        if self.count == 0:
            raise ValueError("Стек пустой")
        return self.top.value

    def is_empty(self) -> bool:
        """
        Проверка, пустой ли стек
        :return: True or False
        """
        return self.count == 0

    def __len__(self) -> int:
        """
        Проверка длины стека
        :return: длина стека
        """
        return self.count

    def min(self) -> int:
        """
        Проверка минимального элемента в стеке
        :return: значение минимального элемента в стеке
        """
        if self.count == 0:
            raise ValueError("Стек пустой")
        return self.stack_inf[-1]
