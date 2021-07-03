# Create a file called 'learning_python.txt' that have a few lines that start
# with the phrase 'In Python you can...'. Write a program that reads the file
# and prints what you wrote three times; once by reading the entire file, once
# by looping over the file object, and once by storing the lines in a list and
# working with it outside the block.
filepath = 'learning_python.txt'
with open(filepath) as file_object:
    contents = file_object.read()

print(f"Read entire file:\n{contents}")
print("\n".rstrip())

with open(filepath) as file_object:
    for line in file_object:
        print(f"Read line by line:\n{line.rstrip()}")

print("\n".rstrip())
with open(filepath) as file_object:
    python_string = ''
    for line in file_object:
        python_string += line

print(f"Store and read:\n{python_string}")
