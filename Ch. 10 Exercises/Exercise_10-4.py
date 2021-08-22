# Write a while loop that prompts users for their name. When they enter their
# name, print a greeting to the screen and add a line recording their visit in a
# file called 'guest_book.txt'. Make sure each entry appears in a new line

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    checking_in = True
    while checking_in:
        patient = input("Please check-in here with your full name, or press 'c'"
                        " to cancel: ")
        if patient.lower() == 'c':
            checking_in = False
        else:
            file_object.write(f"Welcome to Barnabus Hospital, {patient}. The "
                                "doctor will see you soon.\n\n")
