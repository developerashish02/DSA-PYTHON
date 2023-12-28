class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLL:
    def __init__(self):
        self.head = None

    # push using link list

    def push(self, data):

        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = newNode

    # pop using LL
    def top(self):
        # stack is empty
        if self.head is None:
            return "Stack Is Empty"

        # finding the last element
        temp = self.head
        while temp.next != None:
            temp = temp.next

        return temp.data

    def pop(self):
        if self.head is None:
            return "Stack Is Empty"

        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data

        temp = self.head
        prev = None

        while temp.next != None:
            prev = temp
            temp = temp.next

        prev.next = None

        if temp != None:
            return temp.data
        else:
            return "Stack Is Empty"

    def size(self):
        if self.head is None:
            return 0

        count = 0
        temp = self.head

        while temp:
            temp = temp.next
            count += 1

        return count

    def is_empty(self):
        return self.head is None


LL = StackUsingLL()

# LL.push(10)
# LL.push(20)
# LL.push(30)
# LL.push(40)

print(LL.size())

print(LL.pop())

print(LL.size())

print(LL.is_empty())
