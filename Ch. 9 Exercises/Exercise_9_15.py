import random
import string

#### Create User Ticket
def my_ticket_gen(my_ticket, guessing_pool):
    """Generates a new ticket to match against the winning ticket."""
    my_ticket = []
    while len(my_ticket) < 4:
        my_ticket.append(random.choice(guessing_pool))

    return my_ticket

#### Create Winning Ticket
pool = []
while len(pool) < 10:
    n = random.randint(1, 100) # Prevent duplicate numbers in pool
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

#### Iterate user ticket until it matches winning ticket
my_ticket = []
guessing_pool = []

for i in list(string.ascii_lowercase):
    guessing_pool.append(i)

for j in list(range(1, 100)):
    guessing_pool.append(j)

my_ticket = my_ticket_gen(my_ticket, guessing_pool)

won = False
count = 0
max_tries = 1_000_000
while not won:
    count += 1
    if my_ticket == win_set:
        print(f"You won! It took {count} tries!")
        won = True
    elif count >= max_tries:
        break

    my_ticket = my_ticket_gen(my_ticket, guessing_pool)

if won:
    print("Its a match!!!")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {win_set}")
    print(f"It took you {count} tickets to win!")
else:
    print(f"Sorry, no cigars. You went through {count} tickets.")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {win_set}")
