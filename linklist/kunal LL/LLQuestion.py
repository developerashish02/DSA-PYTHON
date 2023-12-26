class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
    # inset at last

    def inset_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node


def displayLL(head):
    curr = head

    while curr != None:
        print(curr.data, end="-> ")
        curr = curr.next

    print("None")


def insert_using_rec(head, pos, data):
    # base case
    if head is None:
        return head

    # small word
    if pos == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    small = insert_using_rec(head.next, pos - 1, data)

    head.next = small

    return head

# remove duplicates


def remove_duplicates(head):
    temp = head
    # edge case
    if temp is None and temp.next is None:
        return temp

    while temp.next != None:
        if temp.data == temp.next.data:
            temp.next = temp.next.next

        else:
            temp = temp.next

    return head


def hasCycle(head) -> bool:

    if head is None:
        return head

    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def hasCycle(head):
    if head is None:
        return 0

    slow = head
    fast = head
    has_cycle = False
    length = 0

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if has_cycle:
        temp = slow.next
        length += 1

        while temp != fast:
            length += 1
            temp = temp.next

        return length
    else:
        return 0


def merge_sorted_array(head1, head2):
    LL = LinkList()
    temp1 = head1
    temp2 = head2

    while temp1 != None and temp2 != None:
        if temp1.data < temp2.data:
            LL.inset_last(temp1.data)
            temp1 = temp1.next

        else:
            LL.inset_last(temp2.data)
            temp2 = temp2.next

    while temp1 != None:
        LL.inset_last(temp1.data)
        temp1 = temp1.next

    while temp2 != None:
        LL.inset_last(temp2.data)
        temp2 = temp2.next

    return LL.head


my_list1 = LinkList()
my_list2 = LinkList()

my_list1.inset_last(90)
my_list1.inset_last(101)
my_list1.inset_last(100)

my_list2.inset_last(70)
my_list2.inset_last(90)
my_list2.inset_last(90)


newHead = merge_sorted_array(my_list1.head, my_list2.head)
# newHead = remove_duplicates(my_list.head)
# head = insert_using_rec(my_list.head, 3, 100)

displayLL(newHead)
