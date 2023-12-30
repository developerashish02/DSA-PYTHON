class Stack:
    def __init__(self):
        self.__stack = []

    # insert a element
    def push(self, item):
        self.__stack.append(item)

    # top most element
    def top(self):
        if len(self.__stack) == 0:
            return "Stack Is Empty"

        else:
            return self.__stack[-1]

    # remove last elements
    def pop(self):
        if len(self.__stack) == 0:
            return "Stack Is Empty"

        else:
            return self.__stack.pop()

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0


class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())

        remove = self.s2.pop()

        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

        return remove

    def peek(self) -> int:
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())

        top = self.s2.top()

        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

        return top

    def empty(self) -> bool:
        return self.s1.is_empty()


obj = MyQueue()
obj.push(10)
obj.push(20)
obj.push(30)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
