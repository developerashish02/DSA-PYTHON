from queue import Queue
from collections import deque


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


def levelOrder(root):
    results = []
    if root is None:
        return results

    my_queue = Queue()
    my_queue.put(root)

    while not my_queue.empty():
        levelSize = my_queue.qsize()
        currentLevelList = []

        for index in range(levelSize):
            currentNode = my_queue.get()
            currentLevelList.append(currentNode.data)

            if currentNode.left is not None:
                my_queue.put(currentNode.left)

            if currentNode.right is not None:
                my_queue.put(currentNode.right)

        results.append(currentLevelList)

    return results


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


def levelOrderSuccessor(root, key):
    if root is None:
        return None

    my_queue = Queue()
    my_queue.put(root)

    while not my_queue.empty():
        currentNode = my_queue.get()

        if currentNode.left != None:
            my_queue.put(currentNode.left)

        if currentNode.right != None:
            my_queue.put(currentNode.right)

        if currentNode.data == key:
            val = my_queue.queue[0]
            return val.data

    return None


def zigZagLevelOrder(root):
    result = []
    if root is None:
        return result

    my_dequeue = deque()
    my_dequeue.append(root)
    reverse = False

    while not my_dequeue:
        levelSize = len(my_dequeue)
        currentLevel = []

        for index in range(levelSize):
            if not reverse:
                currentNode = my_dequeue.popleft()
                currentLevel.append(currentNode.val)

                if currentNode.left != None:
                    my_dequeue.append(currentNode.left)

                if currentNode.right != None:
                    my_dequeue.append(currentNode.right)

            else:
                currentNode = my_dequeue.pop()
                currentLevel.append(currentNode.val)

                if currentNode.right != None:
                    my_dequeue.appendleft(currentNode.right)

                if currentNode.left != None:
                    my_dequeue.appendleft(currentNode.left)

        result.append(currentLevel)
        reverse = not reverse

    return result


def connect(root):
    if root is None:
        return None

    leftNode = root

    while leftNode.right != None:
        currentNode = leftNode
        while currentNode != None:
            currentNode.left.next = currentNode.right

            if currentNode.next != None:
                currentNode.right.next = currentNode.next.left

            currentNode = currentNode.next

        leftNode = leftNode.left

    return root


def findNode(node, x):
    if node is None:
        return node

    if node.data == x:
        return node

    left = findNode(node.left, x)

    if left != None:
        return left

    return findNode(node.right, x)


def findTheLevel(node, x, level):
    if node is None:
        return 0

    if node == x:
        return level

    left = findTheLevel(node.left, x, level+1)

    if left != 0:
        return left

    return findTheLevel(node.right, x, level+1)


def isSiblings(root, x, y):
    if root == None:
        return False

    return (root.left == x and root.right == y) or (root.left == y and root.right == x) or isSiblings(root.left, x, y) or isSiblings(root.right, x, y)


def isCosigns(root, x, y):

    if root is None:
        return False

    xx = findNode(root, x)
    yy = findNode(root, y)

    return (findTheLevel(root, xx, 0) == findTheLevel(root, yy, 0)) and isSiblings(root, xx, yy)


def height(root):
    if root is None:
        return 0

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return leftHeight + rightHeight + 1


def diameterOfBinaryTree(root):
    if root is None:
        return 0

    option1 = height(root.left) + height(root.right)
    option2 = height(root.left)
    option3 = height(root.right)

    return max(option1, max(option2, option3))


root = takeBinaryTreeInput()
xx = findTheLevel(root, 3, 0)
print(xx)
