# Make a list of a series of text messages, and a function called 
# 'show_messages()' to output them.
def show_messages(messages):
    """Displays a series of text messages"""
    for msg in messages:
        print(f"> {msg}")

messages = ["hey when is the party???", "i think i might sleep instead", 
"its at 11!", "you promised you'd come!", "oh dang, fine!"]

show_messages(messages)