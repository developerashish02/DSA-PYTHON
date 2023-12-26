class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def displayLL(self):
        curr = self.head

        while curr != None:
            print(curr.data, end="-> ")
            curr = curr.next

        print("None")

    def inset_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node


def merge(l1, l2):
    ansLL = LinkList()
    temp1 = l1.head
    temp2 = l2.head

    while temp1 != None and temp2 != None:
        if temp1.data < temp2.data:
            ansLL.inset_last(temp1.data)
            temp1 = temp1.next

        else:
            ansLL.inset_last(temp2.data)
            temp2 = temp2.next

    while temp1 is not None:
        ansLL.inset_last(temp1.data)
        temp1 = temp1.next

    while temp2 is not None:
        ansLL.inset_last(temp2.data)
        temp2 = temp2.next

    return ansLL

# cycle 
    def cycle (self)

my_list = LinkList()
my_list.inset_last(10)
my_list.inset_last(20)
my_list.inset_last(30)
my_list.inset_last(40)


my_list_02 = LinkList()

my_list_02.inset_last(100)
my_list_02.inset_last(200)
my_list_02.inset_last(300)
my_list_02.inset_last(400)


ans = merge(my_list, my_list_02)

ans.displayLL()

# my_list.insert_rec(100, 2, my_list.head, None)


# my_list.displayLL()
