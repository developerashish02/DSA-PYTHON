class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
            self.__tail = newNode

            # increase size
            self.__size += 1
            return
        else:
            self.__tail.next = newNode
            self.__tail = newNode
            # increase size
            self.__size += 1

    def front(self):
        if self.__head is not None:
            return self.__head.data
        else:
            return "Queue is Empty"

    def is_empty(self):
        return self.__head is None

    def dequeue(self):
        if self.__head is None:
            self.__tail = None
            return "Queue is empty"

        data = self.__head.data
        self.__head = self.__head.next

        return data


my_queue = QueueLL()

print(my_queue.enqueue(10))
print(my_queue.enqueue(20))
print(my_queue.enqueue(30))
print(my_queue.enqueue(40))


print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

# print(my_queue.is_empty())
