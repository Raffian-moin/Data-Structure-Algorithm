class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

class CircularLinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def display(self, nodes):
        current = nodes
        while current:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break

ll = CircularLinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

ll.head = node1

node1.prev = node3
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node1

ll.display(ll.head)