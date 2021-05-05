##### Store 5 programming related terms in a dictionary with their definitions 
##### as values, then print each one neatly formatted
terms = {
    "conditionals" : "expressions used to handle decisions made by program",
    "loops" : "repeating through sections of code until a certain goal is met",
    "variables" : "storage containing various data and affixed with a label",
    "lists" : "data type used to store multiple values in a single variable",
    "dictionary" : "data type storing various key-value pairs",
}

for val in terms.keys():
    print(f"{val.title()}: {terms[val].capitalize()}\n")