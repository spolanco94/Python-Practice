##### Use the code from 'favorite_languages.py'
##### Make a list of people who should take the favorite languages poll, using 
##### some names already in the dictionary and some that are not
favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "ruby",
    "phil" : "python",
}

should_take_poll = ["jack", "jen", "faruk", "janice", "edward", "sarah"]

##### Loop through the list, and print a message thanking anyone who has taken 
##### it and another message inviting those who haven't to take the poll
for name in should_take_poll:
    if name not in favorite_languages:
        print(f"{name.title()}! Please help our research by taking our short poll!")
    else:
        print(f"{name.title()}, thank you for taking our poll!")