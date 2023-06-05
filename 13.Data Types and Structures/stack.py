"""

What is Stack?
    https://www.youtube.com/watch?v=I37kGX-nZEI&pp=ygUQc3RhY2tzIGV4cGxhaW5lZA%3D%3D

    
Last in First Out    
"""


class Stack:
    def __init__(self) -> None:
        self._items = []

    def isEmpty(self) -> bool:
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self._items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self._items[-1]
        else:
            raise IndexError("Stack is empty")


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.peek())  # Output: 30

    print(stack.pop())   # Output: 30
    print(stack.pop())   # Output: 20

    print(stack.size())  # Output: 1
    print(stack.isEmpty())  # Output: False
