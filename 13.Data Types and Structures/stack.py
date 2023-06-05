"""

What is Stack?
    https://www.youtube.com/watch?v=I37kGX-nZEI&pp=ygUQc3RhY2tzIGV4cGxhaW5lZA%3D%3D

What is a Stack?
    In computer science, a stack is an abstract data type that represents a collection 
    of elements with two principal operations: push and pop. It is commonly referred 
    to as a "last-in, first-out" (LIFO) data structure because the last element added 
    to the stack is the first one to be removed.

    A stack can be visualized as a stack of objects, where new objects are added to the 
    top, and removals also happen from the top. This behavior is analogous to a stack 
    of plates or a stack of books, where you can only add or remove items from the top.

What are the operations available with it?
    Push: 
        This operation adds an element to the top of the stack.

    Pop: 
        This operation removes the topmost element from the stack.

    Peek/Top: 
        This operation retrieves the value of the topmost element in the stack without 
        removing it.

    isEmpty: 
        This operation checks if the stack is empty, i.e., it returns true if there are no 
        elements in the stack and false otherwise.

NOTE: The Python code below goes BEYOND the syllabus
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
