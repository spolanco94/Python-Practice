# Modify the except block from 10-8 to fail silently if either file is missing.

cats = ["lynx", "sphynx", "persian"]
dogs = ["shiba", "shih tsu", "miniature pinscher"]

file_1 = "cats.txt"
file_2 = "dogs.txt"
files = [file_1, file_2]

try:
    for file in files:
        with open(file) as f:
            print(f.read())
except FileNotFoundError:
    pass
