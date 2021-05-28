# Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly
# select four numbers or letters from the list and print a message saying that 
# any ticket matching this combination wins a prize
import random
import string

pool = []
while len(pool) < 10:
    n = random.randint(1,100) # Prevent duplicate numbers in pool
    if n not in pool:
        pool.append(n)

while 10 <= len(pool) < 15:
    # Prevent duplicate letters in pool
    l = random.choice(string.ascii_lowercase) 
    if l not in pool:
        pool.append(l)

win_set = []
while len(win_set) < 4:
    m = random.choice(pool)
    if m not in win_set: # Prevent duplicates in win_set
        win_set.append(m)

print("The winning ticket is: ")
for i in win_set:
    print(f"\t{i}")