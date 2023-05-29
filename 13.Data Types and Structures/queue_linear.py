"""

What is Queue?
    https://www.youtube.com/watch?v=v9BMdz5m5Vo

First In First Out

Involves a lot of moving data

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
