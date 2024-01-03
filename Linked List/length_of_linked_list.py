# Length of the linked list with Iteration

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

    def getLength(self):
        print("Print linked list length")
        length = 0
        current = self.head
        while current:
            current = current.next
            length += 1
            
        print(length)


obj = LinkedList()
obj.addNode(1)
obj.addNode(2)
obj.addNode(3)
obj.addNode(4)
obj.addNode(5)
obj.display()
obj.getLength()

# Linked list length with recursion
print("Linked List with recursion")
class NodeRecursion:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedListRecursion:
    def __init__(self) -> None:
        self.head = None

    def addNode(self, data):
        node = NodeRecursion(data)
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

    def getLength(self, node):
        if not node:
            return 0
        return 1 + self.getLength(node.next)
    
    def getLengthWithTailRecursion(self, node, count=0):
        if not node:
            return count
        return self.getLengthWithTailRecursion(node.next, count + 1)

obj1 = LinkedListRecursion()
obj1.addNode(1)
obj1.addNode(2)
obj1.addNode(3)
obj1.display()

print("Print linked list length with recursion")
print(obj1.getLength(obj1.head))

print("Print linked list length with tail recursion")
print(obj1.getLengthWithTailRecursion(obj1.head))