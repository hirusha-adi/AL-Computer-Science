
# Author: OMKAR PATHAK
# Source Code: https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Linked%20Lists/DoublyLinkedList.py
# NOTE: This is a modified, improved version

class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.prev = previous

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

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
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    # deleting a node from linked list
    def delete(self, data):
        temp = self.head
        if(temp.next != None):
            # if head node is to be deleted
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
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
    
    # for printing the contents of linked lists
    def printdll(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=' ')
            temp = temp.next
    
    def add_at_middle(self, data):
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
    dll = DoublyLinkedList()
    dll.insertAtStart(1)
    dll.insertAtStart(2)
    dll.insertAtEnd(3)
    dll.insertAtStart(4)
    dll.printdll()
    dll.delete(2)
    print()
    dll.printdll()
