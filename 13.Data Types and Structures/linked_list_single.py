"""

Made up of nodes that consists of two parts
    Data - contains actual data
    Link - contains address of the next node

Memmory Addresses aren't stored contiguosly in RAM

eg:

    1            2             3            4                   (Node)
    23 - 2000    54 - 3000     78 - 4000    90 - NULL           (Data-Link)
    (1000)       (2000)        (3000)       (4000)              (Address)

    But, how can we access the first item?

    (Head)                             (Tail)
    Head    1            2             3            4                   (Node)
    1000    23 - 2000    54 - 3000     78 - 4000    90 - NULL           (Data-Link)
            (1000)       (2000)        (3000)       (4000)              (Address)

    The first node called "Head" has no Data value
    it just points to the the second node
        (which is actually the first node with a value)
    
    NULL is called NULL Pointer
        use "-1" as the null pointer

    If the linked list is empty, the Start Pointer will be
    pointed to the NULL pointer as there is no data


NOTE: The Python code below goes BEYOND the syllabus
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def add_at_middle(self, data, position):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        elif position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 1

            while count < position and current.next is not None:
                current = current.next
                count += 1

            new_node.next = current.next
            current.next = new_node

    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    def remove(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


if __name__ == "__main__":
    # Usage example
    linked_list = LinkedList()
    linked_list.add_at_head(3)
    linked_list.add_at_head(2)
    linked_list.add_at_head(1)
    linked_list.add_at_tail(4)
    linked_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> None
    print(linked_list.search(3))  # Output: True
    linked_list.remove(2)
    linked_list.display()  # Output: 1 -> 3 -> 4 -> None

    linked_list2 = LinkedList()
    linked_list2.add_at_head(3)
    linked_list2.add_at_head(2)
    linked_list2.add_at_head(1)
    linked_list2.add_at_middle(5, 1)
    linked_list2.display()  # Output: 1 -> 5 -> 2 -> 3 -> None
