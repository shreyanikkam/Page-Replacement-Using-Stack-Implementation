"""
OPT.py
Description: This file holds the logic for optimal page replacement algorithm
"""

# Importing the queue data structure
from src.Queue import Queue


# This class contains the attributes and methods required to implement optimal page replacement
class OptimalPageReplacement:

    # Default constructor
    def __init__(self, page_sequence, num_of_frames):

        # Initializing a list attribute containing the sequence of pages
        self.sequence = []
        self.sequence = page_sequence

        # Initializing the variable holding the number of page faults
        self.page_fault = 0

        # Initializing the variable telling us the number of frames to use
        self.frame_size = num_of_frames

        # Creating the queue data structure to be used
        self.queue = Queue()

    # Function used to execute the logic for optimal page replacement
    def run(self):

        # Iterating through pages getting the values indexes of those values
        for position, i in enumerate(self.sequence):

            # Checking to see if there is place to insert a page in a frame
            # If there is space
            if self.queue.size() < int(self.frame_size):

                # Next we check if the page is already present in the frames
                try:
                    position = self.queue.find(i)
                    # If the page is present, just display the status of the frames and the pages in them
                    self.display(i)
                except ValueError:
                    # We insert the page into the queue since there is place
                    self.queue.enqueue(i)
                    # Display the current status fo the frames
                    self.display(i)
                    # Incrementing page fault as we are inserting an page into the frame
                    self.page_fault += 1

            # If there is no space
            else:

                # Next we check if the page is already present in the frames or not
                try:
                    position = self.queue.find(i)
                    # if the page is already present then, just display the current status of the frames and the pages
                    self.display(i)
                except ValueError:
                    # We get the position of the page in the list
                    page_position = position
                    # We call the check future use function to check for the page that is used the least in the future
                    self.check_future_page_use(page_position)
                    # Then we insert the new page to the frames
                    self.queue.enqueue(i)
                    # Display the current status of the frames
                    self.display(i)
                    # Incrementing the number of page faults because we are inserting a page into the frames
                    self.page_fault += 1

    # Function used to display the current status of the frames and their values
    def display(self, page):

        # Initializing the status string variable
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

        # Finally we remove the last comma from status string and adding the closing angular bracket instead
        status_string = status_string[0:len(status_string)-2]
        status_string += ">"

        # Printing the status string
        print(status_string)

    # Function to used to check for pages that aren't used in the future as much
    def check_future_page_use(self, page_index):

        # Creating a dictionary to hold the details of the pages and their future usage
        page_usage_details = dict()

        # Using the page_index + 1 we convert the rest of the list into a string
        temp_string_one = str(self.sequence[page_index+1:len(self.sequence)])

        for i in self.queue.items:

            # Finding the first occurrence of the page already present in the queue
            position = temp_string_one.find(i)

            # If it not found then you store the page and and the position as zero
            if position == -1:
                position = None
                page_usage_details[i] = position
            # If it found then you store the page and the position that is returned
            else:
                page_usage_details[i] = position

        print("future pages and their positions ",page_usage_details)

        # Counter to keep track of how locations we have found
        counter = 0

        # Iterating through the dictionary
        for key, value in page_usage_details.items():
            # If we have found a location
            if value is not None:
                counter += 1

        # Checking the counter to see if type of situation we have got
        # if we have the position of all the pages already in the frame
        if counter == self.queue.size():

            # Then we get the furthest position in the string
            max_key = max(page_usage_details.keys(), key=(lambda key: page_usage_details[key]))[0]
            # remove the page with the furthest position value
            self.queue.remove(max_key)

        # if we have found one page that is not used in the future
        elif counter == self.queue.size()-1:
            # find the page with the none value and then remove it
            for key, value in page_usage_details.items():
                if value is None:
                    self.queue.remove(key)
                    break

        # if there are two or more pages that cannot be found use FIFO
        elif counter >= self.queue.size()-2:

            # Creating a temporary dictionary
            temp_dict = dict()

            # we take the first half of the sequence from teh new value found for this condition
            temp_string_two = str(self.sequence[0:page_index])

            # among the none values we see has the lowest occurrence
            for key, value in page_usage_details.items():

                # if the value is none find its position in the temp string two
                if value is None:
                    # finding the position of the value
                    position = temp_string_two.rfind(key)
                    # adding the page and its position to the temporary dictionary
                    temp_dict[key] = position

            # After deciding which page to replace using FIFO we replace the page
            self.queue.remove(min(temp_dict.keys(), key=lambda key:temp_dict[key]))
