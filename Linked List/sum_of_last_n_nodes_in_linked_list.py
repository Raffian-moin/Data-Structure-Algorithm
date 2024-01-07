# Make middle of the linked list head node
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
    def sumOfLastNNodes(self, nNode):
        current = self.head
        firstNodeOfLastNNodes = self.head
        totalNode = 1
        nodesSum = 0
        
        while current:
            nodesSum += current.data
            if totalNode > nNode:
                nodesSum -= firstNodeOfLastNNodes.data
                firstNodeOfLastNNodes = firstNodeOfLastNNodes.next

            current = current.next
            totalNode += 1
        return nodesSum
        

obj = LinkedList()
obj.addNode(1)
obj.addNode(2)
obj.addNode(3)
obj.addNode(4)
obj.addNode(5)
obj.addNode(6)
# obj.display()
print(obj.sumOfLastNNodes(3))
# obj.display()