class Stack_lst:
    def __init__(self) -> None:
        """
        Инициализация объектов класса
        """
        self.list = []
        self.stack_inf = []

    def push(self, x: int) -> None:
        """
        Добавления элемента в стек
        :param x: числовое значение элемента
        :return: None
        """
        self.list.append(x)
        if len(self.stack_inf) == 0:
            self.stack_inf.append(x)
        else:
            self.stack_inf.append(min(x, self.stack_inf[-1]))

    def pop(self) -> int:
        """
        Удаление верхнего элемента в стеке
        :return: None
        """
        if len(self.list) == 0:
            raise ValueError("Стек пустой")
        self.stack_inf.pop()
        return self.list.pop()

    def peek(self) -> int:
        """
        Проверка верхнего элемента в стеке
        :return: значение верхнего элемента в стеке
        """
        if len(self.list) == 0:
            raise ValueError("Стек пустой")
        return self.list[-1]

    def is_empty(self) -> bool:
        """
        Проверка, пустой ли стек
        :return: True or False
        """
        return len(self.list) == 0

    def __len__(self) -> int:
        """
        Проверка длины стека
        :return: длина стека
        """
        return len(self.list)

    def min(self) -> int:
        """
        Проверка минимального элемента в стеке
        :return: значение минимального элемента в стеке
        """
        if len(self.list) == 0:
            raise ValueError("Стек пустой")
        return self.stack_inf[-1]
