class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    # adding new node after the last node
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    # adding new node before the first node
    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    # adding new node in any position
    def insert(self, position, value):
        node = Node(value)
        if position == 1:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            current_position = 1
            while current_position < position-1:
                current = current.next
                current_position += 1

            node.next = current.next
            current.next = node

    # display nodes
    def display(self, linkedList):
        current = linkedList
        while current:
            print(current.data, end=" ")
            current=current.next
        print()    

# creating linked list
ll = LinkedList()

# adding node after the last node
ll.append(1)
ll.append(2)
ll.append(3)
ll.display(ll.head)

ll.append(4)
ll.append(5)
ll.display(ll.head)

# adding node before the first node
ll.prepend(0)
ll.display(ll.head)

# adding node in any position
ll.insert(3, 11)
ll.insert(3, 12)
ll.insert(8, 12)
ll.display(ll.head)

ll.insert(1, -1)
ll.display(ll.head)

ll.insert(11, 100)
ll.display(ll.head)
