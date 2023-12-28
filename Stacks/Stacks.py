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


# Objects
stack = Stack()

print(stack.top())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack.is_empty())
