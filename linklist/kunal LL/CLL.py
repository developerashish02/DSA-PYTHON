class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    # inset in link list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node
        new_node.next = self.head

    # print link list

    def display(self):
        temp = self.head

        if temp is None:
            return

        while True:
            print(temp.data, end="->")
            temp = temp.next

            if temp == self.head:
                break

# objects


my_list = LinkList()

my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.insert(140)


my_list.display()
