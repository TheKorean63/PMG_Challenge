# PMG Coding Challenge
# CSV Combiner

import csv
import sys
import os

def merge_csv_files(files):
    # Creates an empty list to store the rows from each file
    rows = []

    # Loop through each file
    for file in files:
        # Get the basename of the file
        basename = os.path.basename(file)
        
        # Open the file to read
        with open(file, 'r') as i:
            
            # Creates the CSV reader object
            reader = csv.reader(i)

            # Gets the header row
            headers = next(reader)

            # Adds the new header column for the filename
            headers.append('filename')

            # Loops through every row in the file
            for row in reader:
                # Adds the basename to the end of each row
                row.append(basename)
                # Appends the rows to the dictionary created at the beginning
                rows.append(row)

    # Creates the CSV writer object and will create an output dependent on the command line input
    # CL example - python main.py accessories.csv clothing.csv > ***merge.csv***
    writer = csv.writer(sys.stdout)

    # Writes the header row to the output file
    writer.writerow(headers)

    # Writes every row stored in the list to the output file
    for row in rows:
        writer.writerow(row)

# Handles the command line input
# First argument is the name of the script, filenames after, and > output file name at the end
if __name__ == '__main__':
    # Takes any file input after the first argument. The first argument for the command line 
    # is main.py, the script running. Anything after that is file inputs.
    file_input = sys.argv[1:]
    merge_csv_files(file_input)