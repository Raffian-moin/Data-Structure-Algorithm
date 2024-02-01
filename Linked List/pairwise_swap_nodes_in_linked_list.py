class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def display(self, linkedList):
        current = linkedList
        while current:
            print(current.data)
            current=current.next

    def swapNodePairs(self):
        current = self.head
        prev = None
        while current and current.next:

            firstNode = current
            secondNode = current.next

            if prev == None:
                self.head = secondNode
            else:
                prev.next = secondNode

            firstNode.next = secondNode.next
            secondNode.next = firstNode
            prev = firstNode
            current = firstNode.next

# creating linked list
ll = LinkedList()

# creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
# node4 = Node(4)

# joining nodes
ll.head = node1
node1.next = node2
node2.next = node3
# node3.next = node4

# display nodes's value
ll.display(ll.head)
ll.swapNodePairs()
ll.display(ll.head)
