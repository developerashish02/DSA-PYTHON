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

    # delete at nth index
    def delete_nth_index(self, index):
        if index == 0:
            return self.delete_first()

        temp = self.head
        prev = None
        count = 0

        while temp != None and count != index:
            prev = temp
            temp = temp.next
            count += 1

        if temp is None:
            return "Index out of bounds"

        val = prev.next.data
        prev.next = prev.next.next

        return val

    # delete first
    def delete_first(self):

        if self.head is None:
            return "Link list is empty"

        delete_node = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return delete_node

    # delete last
    def delete_last(self):

        if self.head.next is None:
            return self.delete_first()

        temp = self.head
        prev = None

        while temp.next != None:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None

        return temp.data

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

    # insert at nt position
    def insert_nth_position(self, data, index):
        newNode = Node(data)

        # insert at 0 index
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        temp = self.head
        prev = None
        count = 0

        while temp != None and count != index:
            prev = temp
            temp = temp.next
            count += 1

        prev.next = newNode
        newNode.next = temp


# ---------------------------------------Objects --------------------------------------- #
my_list = LinkList()
my_list.inset_last(10)
my_list.inset_last(20)
my_list.inset_last(30)
my_list.inset_last(40)

# my_list.insert_nth_position(100, 1)
# my_list.delete_first()
# ans = my_list.delete_last()

my_list.displayLL()
ans = my_list.delete_nth_index(3)
print("Deleting Last Node is : ", ans)
my_list.displayLL()
