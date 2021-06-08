# Make a program that will count the number of times the word "the" appears in
# a few of the books downloaded from Project Gutenberg
filenames = ["Jekyll-and-Hyde.txt", "Dracula.txt", "The-Great-Gatsby.txt",
            "Pride-And-Prejudice.txt"]

for file in filenames:
    try:
        with open(file, encoding='utf-8') as f:
            count_1 = f.read().lower().count("the")
            print(f"'the' appears approximately {count_1} times in {file}.")
    except FileNotFoundError:
        print(f"Sorry, a file by the name of {file} could not be found.")