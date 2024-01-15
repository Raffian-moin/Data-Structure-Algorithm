# Queue implementation using List
queue = []

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.pop(0)
queue.pop(0)
print(queue)


# Queue implementation using Linked List
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.rear == None:
            self.front = self.rear = node 
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            print('No data to deque')
            return

        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None

        print(temp.data, "is dequeued")
        return
    
    def display(self):
        current = self.front
        while current:
            print(current.data)
            current=current.next 

queue = Queue()
queue.enqueue(1)   
queue.enqueue(2)   
queue.enqueue(3)   
queue.enqueue(4)
queue.display()
queue.dequeue()    
queue.dequeue()    
queue.dequeue()    
queue.dequeue()    
queue.dequeue()
queue.display()
queue.enqueue(1)
queue.display()     
