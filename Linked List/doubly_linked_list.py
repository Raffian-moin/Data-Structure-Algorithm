class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def display(self, linkedList):
        current = linkedList
        while current:
            print(current.data)
            current=current.next


ll = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

ll.head = node1
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

ll.display(ll.head)