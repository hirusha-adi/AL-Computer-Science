"""

What is Queue?
    https://www.youtube.com/watch?v=v9BMdz5m5Vo

First In First Out

What is this?
    A queue is a linear data structure that follows the First-In-First-Out (FIFO) 
    principle, which means that the first element added to the queue will be the 
    first one to be removed. It can be visualized as a line of people waiting for 
    their turn, where the person who arrives first gets served first.

    In a queue, new elements are added at one end called the rear or tail, and elements 
    are removed from the other end called the front or head. This behavior is known 
    as enqueueing (adding) and dequeueing (removing) elements from the queue.

What are the operations associated with it?
    Enqueue: 
        Adds an element to the rear of the queue.
    
    Dequeue: 
        Removes the element from the front of the queue.
    
    Front: 
        Returns the element at the front without removing it.
    
    IsEmpty: 
        Checks if the queue is empty.
    
    Size: 
        Returns the number of elements in the queue.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek into an empty queue.")
        return self.queue[0]


if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    print(my_queue.dequeue())  # Output: 1
    print(my_queue.size())  # Output: 2
    print(my_queue.peek())  # Output: 2
    print(my_queue.is_empty())  # Output: False
