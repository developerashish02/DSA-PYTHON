class Queue:
    # here we keep it queue array is private no one can access the directly
    def __init__(self):
        self.__queue = []

    def enqueue(self, data):
        self.__queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"

        return self.__queue.pop(0)

    def is_empty(self):
        return len(self.__queue) == 0

    def top(self):
        if self.is_empty():
            return "Stack is empty"

        return self.__queue[0]

    def size(self):
        return len(self.__queue)


my_queue = Queue()

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
