# creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # inset first
    def insetFirst(self, data):
        # creating a new node
        node = Node(data)
        node.next = self.head
        self.head = node

        if self.tail is None:
            self.tail = self.head

        self.size += 1

    # display list

    def displayLL(self):
        curr = self.head

        while curr != None:
            print(curr.data, end="-> ")
            curr = curr.next

        print("None")

    # inset at last
    def inset_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node


# ---------------------------------------Objects --------------------------------------- #

my_list = LinkList()
my_list.inset_last(10)
my_list.inset_last(20)
my_list.inset_last(30)
my_list.inset_last(40)

my_list.displayLL()
