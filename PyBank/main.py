# Store the file path associated with the file (note the backslash may be OS specific)
file = 'C:\Users\Brian\UNCCHAR201808DATA3\homework\03-Python\Instructions\PyBank\Resources\budget_data.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)
