"""
NOTE: This topic is COMPLETELY beyond the syllabus

How does it work?
    consists of a sequence of nodes, where each node contains two pointers or references: 
        one pointing to the previous node and 
        one pointing to the next node. 
    this allows for traversal in both directions, making it different 
    from a singly linked list, which only allows forward traversal

What are the main characteristics?
    Nodes: 
        Each node in a doubly linked list contains two pointers, usually called 
        "prev" and "next," which point to the previous and next nodes, respectively. 
        In addition to the pointers, a node also holds the actual data or value 
        associated with it.
    
    Head and Tail: 
        A doubly linked list typically has a reference to the first node, called the 
        "head," and a reference to the last node, called the "tail." These references 
        help in efficiently traversing the list from both ends.

    Bidirectional Traversal: 
        The double linked list allows for traversal in both directions. Starting from 
        the head, you can move forward by following the "next" pointers or move backward 
        by following the "prev" pointers. This flexibility enables operations like 
        searching, inserting, and deleting nodes in both directions.

    Dynamic Size: 
        Unlike arrays, which have a fixed size, a doubly linked list can dynamically 
        grow or shrink as elements are added or removed. This makes it more flexible for 
        managing data that may change frequently.

    Insertion and Deletion: 
        Insertion and deletion of nodes in a double linked list are relatively efficient. 
        When inserting a new node, you simply update the adjacent nodes' pointers to link 
        the new node correctly. Similarly, when deleting a node, you update the adjacent
        nodes' pointers to bridge the gap created by removing the node.

    Memory Overhead: 
        One drawback of a doubly linked list is the additional memory required to store the 
        extra pointers. Compared to a singly linked list, which only requires one pointer 
        per node, a doubly linked list requires two pointers per node, increasing the overall 
        memory overhead.
    
"""
# Author: OMKAR PATHAK
# Source Code: https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Linked%20Lists/DoublyLinkedList.py
# NOTE: This is a modified, improved version


class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.prev = previous


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None

    # SUPPORT FUNCTIONS
    # -----------------------------------------------

    # deleting a node from linked list
    def delete(self, data):
        temp = self.head
        if (temp.next != None):
            # if head node is to be deleted
            if (temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while (temp.next != None):
                    if (temp.data == data):
                        break
                    temp = temp.next
                if (temp.next):
                    # if element to be deleted is in between
                    temp.prev.next = temp.next
                    temp.next.previous = temp.prev
                    temp.next = None
                    temp.prev = None
                else:
                    # if element to be deleted is the last element
                    temp.prev.next = None
                    temp.prev = None
                return

        if (temp == None):
            return

    # print the contents of the linked list
    def printdll(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end=' ')
            temp = temp.next

    # check if double linked list is empty
    def is_empty(self):
        return self.head is None

    # ACTION FUNCTIONS
    # -----------------------------------------------

    # for inserting at beginning of linked list
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    # for inserting at end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    # for inserting at the middle of linked list
    def insertAtMiddle(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node
        else:
            slow_ptr = self.head
            fast_ptr = self.head.next

            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

            new_node.next = slow_ptr.next
            new_node.prev = slow_ptr
            slow_ptr.next = new_node
            if new_node.next is not None:
                new_node.next.prev = new_node
            else:
                self.tail = new_node


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insertAtStart(1)
    dll.insertAtStart(2)
    dll.insertAtEnd(3)
    dll.insertAtStart(4)
    dll.printdll()
    dll.delete(2)
    print()
    dll.printdll()
