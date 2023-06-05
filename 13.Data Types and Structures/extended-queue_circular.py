"""
NOTE: This topic is COMPLETELY beyond the syllabus

What is a Circular Queue?
    https://www.youtube.com/watch?v=8sjFA-IX-Ww
    https://www.youtube.com/watch?v=dn01XST9-bI

Brings fix to:
    involves a lot of moving data in linear queues
    
Eventually the queue will 'wrap around' to the beginning
"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Unable to enqueue item.")
            return
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue item.")
            return None
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        elif self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()


if __name__ == "__main__":
    queue = CircularQueue(5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)  # Queue is full. Unable to enqueue the itme.

    queue.display()  # Outputs: 1 2 3 4 5

    queue.dequeue()
    queue.dequeue()

    queue.display()  # Outputs: 3 4 5
