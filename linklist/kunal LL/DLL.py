class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self):
        self.head = None

    # insert first
    def inset_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head != None:
            self.head.prev = new_node

        self.head = new_node

    # print DLL

    def display_forward(self):
        temp = self.head

        while temp != None:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def display_backword(self):
        temp = self.head

        while temp.next != None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end="->")
            temp = temp.prev

        print("None")


my_list = LinkList()
my_list.inset_first(10)
my_list.inset_first(20)
my_list.inset_first(30)
my_list.inset_first(40)

my_list.display_forward()

my_list.display_backword()
