"""
Queue.py
Description: This file contains the implementation of the queue data structure
"""

# The queue class is used to implement functionality of a queue using a list
class Queue:

    # Default constructor
    def __init__(self):
        self.items = []

    # Function used to tell us if the queue is empty
    def isEmpty(self):
        return self.items == []

    # Function used to add an item to the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # Function used to remove an item from the queue
    def dequeue(self):
        return self.items.pop()

    # Function used to return the size of the queue
    def size(self):
        return len(self.items)

    # Function used to check whether a value exists or not
    def find(self, item):
        return self.items.index(item)

    # Function used to return the value at the particular position
    def get(self, pos):
        return self.items[pos]

    # Function used to remove an item from the queue
    def remove(self, item):
        self.items.remove(item)
