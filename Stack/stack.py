# Stack implementation using List
stack = []

def push(data):
    stack.append(data)

def pop():
    if not isEmpty():
        print(stack[len(stack)-1], "is popped")
        stack.pop()

def peek():
    if not isEmpty():
        print(stack[len(stack)-1], "is the top element")

def isEmpty():
    if len(stack) == 0:
        return True

push(1)
push(2)
print(stack)
pop()
peek()
print(stack)



# Stack implementation using Linked List
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head != None:
            node.next = self.head

        self.head = node

    def displayStack(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()
            
    def pop(self):
        if (not self.isEmpty()):
            print(self.head.data, "is popped")
            self.head = self.head.next
        else:
            print("Stack is empty!")

    def isEmpty(self):
        if self.head == None:
            return True

    def peek(self):
        if (not self.isEmpty()):
            print(self.head.data, "is the top element")
        else:
            print("Stack is empty!")
        

obj = Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.displayStack()
obj.pop()
obj.peek()
obj.displayStack()