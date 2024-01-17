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


def depthOfNode(root, k):
    # if we have the root then work
    if k == 0:
        print(root.data)
        return

    for index in range(len(root.children)):
        depthOfNode(root.children[index], k - 1)


def countLeafNodes(root):
    if root is None:
        return 0

    # small word
    if len(root.children) == 0:
        return 1

    count = 0

    # recursion call
    for index in range(len(root.children)):
        count += countLeafNodes(root.children[index])

    return count


def preOrder(root):
    if root is None:
        return

    print(root.data, end=" ")

    for index in range(len(root.children)):
        preOrder(root.children[index])


def postOrder(root):
    if root is None:
        return

    for index in range(len(root.children)):
        postOrder(root.children[index])

    print(root.data, end=" ")


def containsX(root, x):
    if root is None:
        return False

    if root.data == x:
        return True

    for index in range(len(root.children)):
        smallAns = containsX(root.children[index])

    return smallAns


# objects
root = takeInput()
# printTree(root)

# # count = countNodes(root)
# ans = countLeafNodes(root)

# print("The Number of Nodes : ", ans)

postOrder(root)
