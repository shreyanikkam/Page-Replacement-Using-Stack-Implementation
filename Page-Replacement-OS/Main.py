# Importing the FirstInFirstOut class from the FIFO.py file
from src.FIFO import FirstInFirstOut

# Importing the LeastRecentlyUsed class from the LRU.py file
from src.LRU import LeastRecentlyUsed

# Importing the OptimalPageReplacement class from the OPT.py file
from src.OPT import OptimalPageReplacement

# We open the input file in read mode and initialize the file object 
file_object = open(" C:\Users\Shreya Nikkam\Desktop\InputFile2.txt", "r")   

# Reading the first line 
input_string = file_object.readline()

# We close the file object
file_object.close()

# We get the number of frames  from the input string
num_of_frames = input_string[2:3]

# We get the first character from the input string so that we may know which algorithm to call
algorithm_to_use = input_string[0:1]

# Removing the first character and comma from the input string and initialize the temp string
temp_string = input_string[4:]

# Creating a list called page sequence by splitting the temp string
page_sequence = temp_string.split(",")

# If first character is F then we execute the first in first out algorithm
if algorithm_to_use == "F":

    # Printing the algorithm for which we are executing the logic
    print("For FIFO \n")
    # Initializing the data required to begin executing the FIFO algorithm
    page_replacement = FirstInFirstOut(page_sequence, num_of_frames)
    # executing FIFO page replacement algorithm
    page_replacement.run()
    # Printing the number of page faults
    print("\nThe number of page faults using FIFO is ", page_replacement.page_fault)

# If first character is O then we execute the optimal page algorithm
elif algorithm_to_use == "O":

    # Printing the algorithm for which we are executing the logic
    print("For OPT \n")
    # Initializing the data required to begin executing the OPT algorithm
    page_replacement = OptimalPageReplacement(page_sequence, num_of_frames)
    # executing the OPT page replacement algorithm
    page_replacement.run()
    # Printing the number of page faults
    print("\nThe number of page faults using OPT is ", page_replacement.page_fault)

# If first character is L then we execute the least recently used algorithm
elif algorithm_to_use == "L":

    # Printing the algorithm for which we are executing the logic
    print("For LRU \n")
    # Initializing the data required to begin executing the LRU algorithm
    page_replacement = LeastRecentlyUsed(page_sequence)
    # executing the LRU page replacement algorithm
    page_replacement.run()
    # Printing the number of page faults
    print("\nThe number of page faults using LRU is ", page_replacement.page_fault)
