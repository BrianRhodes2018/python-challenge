# Store the file path associated with the file (note the backslash may be OS specific)
file = '9bb5ed3cd7c611280045ee597a27879d0e6daff6'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)
