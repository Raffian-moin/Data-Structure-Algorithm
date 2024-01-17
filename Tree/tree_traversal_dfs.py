class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def inOrder(self, root):
        if root:
            if root.left:
                self.inOrder(root.left)

            print(root.data, end="->")

            if root.right:
                self.inOrder(root.right)

    def preOrder(self, root):
        if root:
            print(root.data, end="->")

            if root.left:
                self.preOrder(root.left)

            if root.right:
                self.preOrder(root.right)

    def postOrder(self, root):
        if root:
            if root.left:
                self.postOrder(root.left)

            if root.right:
                self.postOrder(root.right)

            print(root.data, end="->")
            
node1 = Node(1)
node2 = Node(12)
node3 = Node(5)
node4 = Node(6)
node5 = Node(9)

root = node1
root.left = node2
root.right = node5
root.left.left = node3
root.left.right = node4

obj = Tree()
obj.inOrder(root)
print()
obj.preOrder(root)
print()
obj.postOrder(root)