# This class is used to implement a stack which in turn is used to implement LRU
class Stack:

    # Default constructor
    def __init__(self):
        self.items = []

    # Function used to push an item on to the stack
    def push(self, item):
        self.items.append(item)

    # Function used to remove the item from the top of the stack
    def pop(self):
        return self.items.pop()

    # Function used to return the position of the item at the top of the list
    def peek(self):
        return self.items[len(self.items) - 1]

    # Function used to return the size of the stack
    def size(self):
        return len(self.items)

    # Function used to find an item in the stack
    def find(self, item):
        return self.items.index(item)

    # Function to remove a page from the stack
    def remove(self, item):
        self.items.remove(item)


# This class holds the attributes and methods for the least recently used page replacement
class LeastRecentlyUsed:

    # Default constructor
    def __init__(self, page_sequence):

        # Initializing a sequence list filled with the pages
        self.sequence = page_sequence

        # Creating a stack that we have to use
        self.stack = Stack()

        # Setting the number of page faults to zero in the beginning
        self.page_fault = 0

    # Function used to execute the logic for least recently used page replacement algorithm
    def run(self):

        # Iterating through the sequence of pages
        for i in self.sequence:

            # This variable tells us whether the page is present in the stack or not
            present_flag = False

            # First we check to see if page is present in the stack or not
            try:
                position = self.stack.find(i)
                # If the page is present in the stack we set the flag to true
                present_flag = True
            except ValueError:
                pass

            # If the page is already present
            if present_flag:
                # Then we remove the item from its position in the stack
                self.stack.remove(i)
                # Then we re insert the item to the stack again
                self.stack.push(i)
                # Display the current status of the stack
                self.display(i)
            # Else if the page is not present
            else:
                # We add the page to stack
                self.stack.push(i)
                # Display the current status of the stack
                self.display(i)
                # Increment the page fault by one
                self.page_fault += 1

    # Function used to display the status of the frames and the pages in them
    def display(self, page):

        # The frames of pages into a string and removing the first and last square brackets
        current_stack_status  = str(self.stack.items)[1:-1]
        # Printing the status of the stack
        print(page+": <"+current_stack_status+">")
