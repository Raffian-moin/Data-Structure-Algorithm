# Reverse Linked List using Iterative and Recursion
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def display(self):
        print("Print items")
        current = self.head
        while current:
            print(current.data)
            current=current.next

    # Iterative Method
    def findNthNodeFromEnd(self, nodePositionFromEnd):
        current = self.head
        targetNode = self.head
        position = 0
        
        while current:
            current = current.next
            position += 1
            if position > nodePositionFromEnd:
                targetNode = targetNode.next

        if (position < nodePositionFromEnd):
            return 'No data found'
        
        return targetNode.data

obj = LinkedList()
obj.addNode(1)
obj.addNode(2)
obj.addNode(3)
obj.addNode(4)
obj.addNode(5)
obj.display()
print(obj.findNthNodeFromEnd(6))