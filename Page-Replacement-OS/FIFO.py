# Importing the queue data structure to be used
from src.Queue import Queue

# The FirstInFirstOut class is used to implement
class FirstInFirstOut:

    # Default constructor
    def __init__(self, page_sequence, num_of_frames):

        # Initializing a list attribute of page sequences
        self.sequence = page_sequence

        # Initializing the number of page faults
        self.page_fault = 0

        # Initializing the number off frames
        self.frame_size = num_of_frames

        # Creating a queue to use
        self.queue = Queue()

    # Function used to execute the logic of fifo
    def run(self):

        # Iterating through the page sequence
        for i in self.sequence:

            # Next we check if the queue is full or not
            if self.queue.size() < int(self.frame_size):

                # Checking if the page is present in the queue or not
                try:
                    position = self.queue.find(i)
                    # Display the status of the queue
                    self.display(i)
                except ValueError:
                    # if queue is not full add the page to the queue
                    self.queue.enqueue(i)
                    # display the current status of the queue
                    self.display(i)
                    # If it is not present then increment the page fault
                    self.page_fault += 1

            # If the queue is full pop the first page and add new page at the end
            else:
                # Checking if the page is present in the queue or not
                try:
                    position = self.queue.find(i)
                    # Display the status of the queue
                    self.display(i)
                except ValueError:
                    # Pop the page in front of the queue
                    self.queue.dequeue()
                    # Insert the new page to the queue
                    self.queue.enqueue(i)
                    # Display the status of the queue
                    self.display(i)
                    # If it is not present then increment the page fault
                    self.page_fault += 1

    # function used to display the frame and the pages in them
    def display(self, page):

        # Initializing the status string 
        status_string = page + ": <"

        # Iterating through the frames
        for i in range(int(self.frame_size)):

            # Checking if there is a value at the frame
            try:
                # If there is a value then the status string is updated
                value = self.queue.get(i)
                status_string += value + ", "
                # if there isn't a value then an index error is thrown and the status string is updated
            except IndexError:
                status_string += " " + ", "

        # Finally we remove the last comma from status string 
        status_string = status_string[0:len(status_string)-2]
        status_string += ">"

        # Printing the status string
        print(status_string)
