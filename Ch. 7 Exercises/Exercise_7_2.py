##### Write a program asking for dinner party size. If more than 8, give a wait
##### time.
party_size = input("How big of a party will be dining tonight? ")
party_size = int(party_size)

if party_size > 8 :
    print(f"For a party of {party_size}, there will be a 30 minute waiting "
    "period.")
    response = input("Will that be alright? (y/n) ")
    responded = False

    while not responded:
        if response.lower() == 'y' or response.lower() == 'n':
            responded = True
        else:
            response = input("I am sorry, I do not understand your response. "
            "Please respond with 'y' for yes or 'n' for no. ")

    if response.lower() == "y":
        print("Thank you for your patience. We will notify you once your table "
        "is ready.")
    elif response.lower() == "n":
        print("We understand and hope to service you another time.") 
else: 
    print("Very well, you may follow us to your table now.")