# Use the replace() method to replace any word in a string with a different 
# word. Read each line from the 'learning_python.txt' file and replace the word 
# 'Python' with C.
filename = 'Ch. 10 Exercises\learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        revised = line.replace("Python", "C")
        print(revised)