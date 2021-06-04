# Write a while loop that asks people why the love programming. Everytime they 
# enter a response, write it to a file that will store all of them.
filename = 'programming_poll.txt'

with open(filename, 'w') as file_object:
    polling = True
    while polling:
        response = input("Why do you love programming?\nEnter 'q' to quit.\n")
        if response.lower() == 'q':
            polling = False
        else:
            file_object.write(f"{response}\n\n")