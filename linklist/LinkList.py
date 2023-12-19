class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Print The link list


def printLL(head):
    while head != None:
        print(str(head.data) + "->", end="")
        head = head.next
    print("None")

# Take input of link list


def takeInputLL():
    # List [int(ele) for ele in input().split()] is a list comprehension. It converts each substring (which is a string) into an integer using int(ele) and creates a new list containing these integers.

    inputList = [int(ele) for ele in input().split()]

    # head is initial is none
    head = None
    tail = None

    for currData in inputList:
        # if we reach to the None we stop
        if currData == -1:
            break

        # create a Node
        newNode = Node(currData)

        # after creating a first Node head is pointing to the next node
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

    return head


head = takeInputLL()
printLL(head)
