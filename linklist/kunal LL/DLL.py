class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self):
        self.head = None

    # add in last

    def add_in_last(self, data):

        if self.head is None:
            self.inset_first(data)
            return

        temp = self.head

        while temp.next != None:
            temp = temp.next

        new_node = Node(data)

        new_node.next = None

        if new_node.prev != None:
            new_node.prev = temp

        temp.next = new_node

    # insert first

    def inset_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head != None:
            self.head.prev = new_node

        self.head = new_node

    # print DLL
    # print forwards

    def display_forward(self):
        temp = self.head

        while temp != None:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    # print  backwards
    def display_backward(self):
        temp = self.head

        while temp.next != None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end="->")
            temp = temp.prev

        print("None")


my_list = LinkList()
my_list.add_in_last(10)
my_list.add_in_last(20)
my_list.add_in_last(30)
my_list.add_in_last(40)
my_list.add_in_last(50)

my_list.display_forward()

# my_list.display_backward()
