# Delete Node from Linked List using Iterative and Recursion
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
        print()
        print("Print items")
        current = self.head
        while current:
            print(current.data, end=" ")
            current=current.next

    # Iterative Method
    def deleteNode(self, position):
        current = self.head
        prev = None
        pointerPosition = 1
        while current:
            if pointerPosition == position:
                if position == 1:
                    self.head = current.next
                elif current.next is None:
                    prev.next = None
                else:
                    prev.next = current.next
                break
                    
            prev = current
            current = current.next
            pointerPosition += 1

    # Recursion Method
    def deleteNodeRecursively(self, currentNode, position, prev=None, pointerPosition=1):
        currentNode = currentNode
        nextNode = currentNode.next

        if (pointerPosition == position):
            if position == 1:
                self.head = currentNode.next
            elif nextNode is None:
                prev.next = None
            else:
                prev.next = currentNode.next
            return 1
        
        pointerPosition += 1
        
        return self.deleteNodeRecursively(nextNode, position, currentNode, pointerPosition)
    
    def deleteNodeWrapper(self, position):
        self.deleteNodeRecursively(self.head, position)

obj = LinkedList()
obj.addNode(1)
obj.addNode(2)
obj.addNode(3)
obj.addNode(4)
obj.addNode(5)
obj.display()
obj.deleteNode(3)
obj.deleteNodeWrapper(4)
obj.deleteNodeWrapper(3)
obj.display()