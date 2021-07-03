# Write a polling program asking users about their dream vacation and print the
# results

print("Welcome! We would like to know what some of the most popular vacation "
"destinations are.")
vacation_destination = []
polling = True
counter = {}
while polling:
    response = input("Please tell us where your dream vacation would be. ")
    vacation_destination.append(response)

    print("\nThank you for your response!")
    continue_poll = input("If someone else would like to take the poll, please "
    "enter 'n' for a new query. Otherwise enter 'done' to finish. ")
    if continue_poll.lower() == 'n':
        polling = True
    elif continue_poll.lower() == 'done':
        break

for location_1 in vacation_destination:
    count = 0
    for location_2 in vacation_destination:
        if location_1 == location_2:
            count += 1
            counter[location_1] = count

print("\nHere are the results of the poll:")
for location, total in counter.items():
    print(f"{location.title()}: {total}")
