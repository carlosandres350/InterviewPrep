# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)
        

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)


    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return 
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        #check here
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
        pass

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        #iterate through list until we reach the tail or position
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)


    def removeNodesWithValue(self, value):
        # iterate through list, and search for a node with the value equal to the given value
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
                

    def remove(self, node):
        # check for edge cases
        if node == self.head:
            #if node to remove is the head, then first set the head to be equal to the next value
            self.head = self.head.next
        if node == self.tail:
             #if node to remove is the tail, then first set the tail to be equal to the previous value
            self.tail = self.tail.prev
        self.removeNodeBindings(node)
            

    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        #iterate through linked list and search for value
        while node is not None and node.value != value:
            node = node.next
        #return node is not None, this will return True if the node has a a value, and False if we reached the tail of the list since node is None 
        return node is not None

    def removeNodeBindings(self, node):
        # ensure that were not at the head, or there is a previous value
        if node.prev is not None:
            #point the nodes previous node equal to its next node
            node.prev.next = node.next
        # ensure that were not at the tail, or there is a next value
        if node.next is not None:
            #point the next nodes previous pointer the current nodes previous node
            node.next.prev = node.prev
        # set the current nodes pointers to None , removing it from the list
        node.prev = None
        node.next = None
        