from queue import Queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        return

    print(root.data, ":", end=" ")

    if root.left != None:
        print("L", root.left.data, end=" ")

    if root.right != None:
        print("R",  root.right.data, end=" ")

    print("")

    print_tree(root.left)
    print_tree(root.right)


def takeInput():
    print("Enter Data ", end="")
    rootData = int(input())
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)

    root.left = takeInput()
    root.right = takeInput()

    return root


def takeInputLevelWise():
    rootData = int(input("Enter the root data : "))

    root = BinaryTreeNode(rootData)

    # queue
    pendingNodes = Queue()

    pendingNodes.put(root)


root = takeInput()
print_tree(root)
