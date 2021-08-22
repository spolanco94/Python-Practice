# Make two files, cats.txt and dogs.txt, and store at least 3 kinds of each into
# each file. Write the code in a try-except block that will catch a FileNotFound
# error, or print the contents of each file if there are none.

cats = ["lynx", "sphynx", "persian"]
dogs = ["shiba", "shih tsu", "miniature pinscher"]

file_1 = "cats.txt"
file_2 = "dogs.txt"

with open(file_1, 'w') as f:
    for cat in cats:
        f.write(f"{cat}\n")

# with open(file_2, 'w') as f:
#     for dog in dogs:
#         f.write(f"{dog}\n")

files = [file_1, file_2]
try:
    for file in files:
        with open(file) as f:
            print(f.read())
except FileNotFoundError:
    print(f"Sorry, the file {file} could not be found.")
