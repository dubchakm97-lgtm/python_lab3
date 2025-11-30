class MyStack:

    def __init__(self):
        self.base_q = []
        self.extra_q = []

    def push(self, x: int) -> None:
        self.extra_q.append(x)

        while self.base_q:
            elem = self.base_q.pop(0)
            self.extra_q.append(elem)

        self.base_q, self.extra_q = self.extra_q, self.base_q


    def pop(self) -> int:
        if len(self.base_q) == 0:
            raise ValueError('Стек пустой')
        elem = self.base_q[0]
        self.base_q.pop(0)
        return elem

    def top(self) -> int:
        if len(self.base_q) == 0:
            raise ValueError('Стек пустой')
        return self.base_q[0]

    def empty(self) -> bool:
        return len(self.base_q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
