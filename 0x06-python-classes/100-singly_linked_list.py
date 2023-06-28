#!/usr/bin/python3
# 100-singly_linked_list.py
# DevWambugu
"""Define a class Node.
   defines a node of a singly linked list
"""


class Node:
    '''defines a class node
    defines a node of a singly linked list
    '''

    def __init__(self, data, next_node=None):
        '''Initialize new_Node.

        Args:
            data: new Node data
            next_node: next node of the new_Node.
	'''
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''retrieve the data attribute'''
        return self.__data

    @data.setter
    def data(self, value):
        '''sets the attribute'''
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        '''retrieve attribute'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''set the attribute'''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        '''Private instance attribute: head (no setter or getter)'''
        self.__head = None

    def sorted_insert(self, value):
        '''inserts a new Node into the correct sorted position
        in the list (increasing order)

	Args:
            value: new Node to be insert
        '''
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        '''Return a string representation of the linked list'''
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
