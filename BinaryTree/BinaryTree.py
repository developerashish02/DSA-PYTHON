class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printBinaryTree(root):
    if root is None:
        return

    print(root.data, end=": ")

    if root.left != None:
        print("L",  root.left.data, end=" ")

    if root.right != None:
        print("R", root.right.data, end="")

    print()

    printBinaryTree(root.left)
    printBinaryTree(root.right)

# take binary tree input


def takeBinaryTreeInput():
    rootData = int(input("Enter the data: "))

    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)

    left = takeBinaryTreeInput()
    right = takeBinaryTreeInput()

    root.left = left
    root.right = right

    return root


root = takeBinaryTreeInput()
printBinaryTree(root)
