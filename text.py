class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)

        new_node.next = self.head
        if self.head != None:
            self.head.prev = new_node
        new_node.prev = None
        self.head = new_node

    def insert_last(self, data):
        if self.head is None:
            self.insert_first(data)
            return

        new_node = Node(data)
        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = new_node
        new_node = temp

    def display_forward(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

        print("None")

    def delete_first(self):
        if self.head is None:
            print("List is empty ")
            return

        self.head = self.head.next
        if self.head != None:
            self.head.prev = None


my_list = LinkList()
# my_list.insert_first(10)
# my_list.insert_first(20)
# my_list.insert_first(30)
# my_list.insert_first(40)
my_list.insert_last(10)
my_list.insert_last(20)
my_list.insert_last(30)
my_list.insert_last(40)
my_list.delete_first()

my_list.display_forward()
