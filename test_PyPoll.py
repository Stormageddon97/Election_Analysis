# The data we need to retrieve.
#1. the total number of votes cast
#2. A complete list of candidates who recieved votes 
#3. The percentage of votes each candidate won 
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.



# Assigning a variable to the file path 
#file_to_load = 'Resources/election_results.csv'

# -------------------------------------------------------------------

# Opening the file and reading the file
#election_data = open(file_to_load, 'r')

# To do: This section is going to be filled with the process off performing the analysis       **WHY SHOW ME THIS METHOD THEN IMMEDIATELY SHOW ME A DIFFERENT METHOD!?**


# Following code will close the file
#election_data.close()

# -------------------------------------------------------------------

# -------------------------------------------------------------------


# Open the election results and read the file
#with open(file_to_load) as election_data:                                  **AGAN HERE?**

     # To do: perform analysis.
#     print(election_data)

# ----------------------------------------------------------------------

#--------------------------------------------------------------------------
#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")           **Again**
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
#     print(election_data)

# ----------------------------------------------------------------------


# -------------------------------------------------------------------



# ---------------------------------------------------------------------
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")                       ** Showing me an error?** 

# Close the file
#outfile.close()


# --------------------------------------------------------------------------



# ------------------------------------------------------------------------

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.                    ** Broken example ** 
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
 #   txt_file.write("Hello World")



# -----------------------------------------------


# -----------------------------------------------------------]

    # Create a filename variable to a direct or indirect path to the file.          ** Still broken after fol;ling moduule word for word! **
#file_to_save = os.path.join("analysis", "election_analysis.txt")                       I understand what is supposed to be happening
#                                                                                                But it doesn't 

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

# -----------------------------------------------------------------




# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("election_analysis.txt")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")


# Write three counties to the file.

#outfile.write("Arapahoe\nDenver\nJefferson")



# Close the file
#outfile.close()




# --------------------------------------------

# Time to find external resouces for information 

# ------------------------------------------------


# ***
# IT WAS *IMPORT OS* THIS WHOLE TIME 
# ***




# Create a filename variable to a direct or indirect path to the file.
import os


file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

outfile.write("Arapahoe\nDenver\nJefferson")
txt_file.write("Arapahoe, Denver, Jefferson")

# Close the file
outfile.close()