class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def level_order(root):
    if not root:
        return
    values = []
    queue = []
    queue.append(root)
    while len(queue) > 0:
        values.append(queue[0].info)

        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    output = str(values).replace('[', '').replace(',', '').replace(']', '')
    print(output)


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(6)

    arr = [1, 2, 3, 4, 5, 6]

    for i in range(t):
        tree.create(arr[i])

    level_order(tree.root)
