#!/usr/bin/python3
"""Defines classes for a singly-linked list."""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): Data for the node.
            next_node (Node, optional): Next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initialize an empty singly-linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node in the sorted position.

        Args:
            value (int): Data for the new node to insert.
        """
        new = Node(value)
        if self.__head is None or self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Return a string representation of the list."""
        values = []
        tmp = self.__head
        while tmp:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
