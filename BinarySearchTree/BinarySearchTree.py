from ast import List
from queue import Queue


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelOrder(self, root) -> List[List[int]]:
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
            currentLevelList.append(currentNode.val)

            if currentNode.left is not None:
                my_queue.put(currentNode.left)

            if currentNode.right is not None:
                my_queue.put(currentNode.right)

        results.append(currentLevelList)

    return results


def levelOrderSuccess(root, data):
    if root is None:
        return None

    my_queue = Queue()
    my_queue.put(root)

    while not my_queue.empty():
        levelSize = my_queue.qsize()
        for index in range(levelSize):
            currentNode = my_queue.get()

            if currentNode.val == data:
                if currentNode.left != None:
                    my_queue.put(currentNode.left)

                if currentNode.right != None:
                    my_queue.put(currentNode.right)

                success = my_queue.get()

                return success

    return None
