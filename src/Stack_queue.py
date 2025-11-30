class Stack_q:
    def __init__(self):
        """
        Инициализация объектов класса
        """
        self.base_q = []
        self.extra_q = []
        self.stack_inf = []

    def push(self, x: int) -> None:
        """
        Добавления элемента в стек
        :param x: числовое значение элемента
        :return: None
        """
        self.extra_q.append(x)

        while self.base_q:
            elem = self.base_q.pop(0)
            self.extra_q.append(elem)

        self.base_q, self.extra_q = self.extra_q, self.base_q

        if len(self.stack_inf) == 0:
            self.stack_inf.append(x)
        else:
            self.stack_inf.append(min(x, self.stack_inf[-1]))

    def pop(self) -> int:
        """
        Удаление верхнего элемента в стеке
        :return: None
        """
        if len(self.base_q) == 0:
            raise ValueError("Стек пустой")
        elem = self.base_q[0]
        self.base_q.pop(0)
        self.stack_inf.pop()
        return elem

    def peek(self) -> int:
        """
        Проверка верхнего элемента в стеке
        :return: значение верхнего элемента в стеке
        """
        if len(self.base_q) == 0:
            raise ValueError("Стек пустой")
        return self.base_q[0]

    def is_empty(self) -> bool:
        """
        Проверка, пустой ли стек
        :return: True or False
        """
        return len(self.base_q) == 0

    def __len__(self) -> int:
        """
        Проверка длины стека
        :return: длина стека
        """
        return len(self.base_q)

    def min(self) -> int:
        """
        Проверка минимального элемента в стеке
        :return: значение минимального элемента в стеке
        """
        if len(self.base_q) == 0:
            raise ValueError("Стек пустой")
        return self.stack_inf[-1]
