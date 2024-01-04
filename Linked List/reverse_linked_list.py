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
    def reverseLinkedList(self):
        current = self.head
        previous = None
        
        while current:
            next = current.next
            current.next = previous 
            previous = current
            current = next

        self.head = previous

    # Recursion Method
    def reverseLinkedListRecursively(self, currentNode, prev):
        current = currentNode
        next = current.next
        current.next = prev 
        if (next is None):
            self.head = current
            return
        
        return self.reverseLinkedListRecursively(next, current)
            


obj = LinkedList()
obj.addNode(1)
obj.addNode(2)
obj.addNode(3)
obj.addNode(4)
obj.addNode(5)
obj.display()
obj.reverseLinkedList()
obj.display()
obj.reverseLinkedListRecursively(obj.head, None)
obj.display()