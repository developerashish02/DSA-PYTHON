class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


# take a input
def takeInput():
    rootData = int(input("Enter the data: "))
    rootNode = TreeNode(rootData)

    n = int(input("Enter the number of children of "))

    for num in range(n):
        child = takeInput()
        rootNode.children.append(child)

    return rootNode

# print a tree


def printTree(root):

    if root is None:
        return

    print(root.data, ":", end=" ")

    for index in range(len(root.children)):
        print(root.children[index].data, end=" ")

    print()
    for index in range(len(root.children)):
        printTree(root.children[index])


# count the number of nodes
def countNodes(root):

    ans = 1

    for index in range(len(root.children)):
        ans += countNodes(root.children[index])

    return ans


# objects
root = takeInput()
printTree(root)

count = countNodes(root)

print("The Number of Nodes : ", count)
