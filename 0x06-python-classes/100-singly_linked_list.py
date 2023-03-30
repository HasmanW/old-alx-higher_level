#!/usr/bin/python3
"""
Singly Linked List Node module
"""


class Node:
    """ The node class """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ retrieves a nodes data """
        return self.data

    @data.setter
    def data(self, value):
        """ sets the data in the node """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """ retrieves the next node """
        return self.next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the next node """
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a node object')
        self.next_node = value


class SinglyLinkedList:
    """ the singly linked list class """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """ inserts and sorts a new node """
        new_node = Node(value)

        # check if linked list is empty
        if self.head is None:
            new_node.next_node = None
            self.head = new_node
        # check if data head is pointing is greater than value
        elif self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        # check for favourable position
        else:
            current_node = self.head
            while current_node.next_node is not None and value > current_node.data:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next_node is not None:
            elements.append(current_node.data)
        return elements


