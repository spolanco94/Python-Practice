# Expand the code from 8-9 to move each message to a new list called
# 'sent_messages'. Print both lists to make sure everything moved correctly.

def show_messages(messages, sent_messages):
    """Displays a series of text messages"""
    while messages:
        curr = messages.pop()
        print(f"> {curr}")
        sent_messages.append(curr)

    sent_messages.reverse()
    print(f"Messages: {messages}")
    print(f"Sent messages: {sent_messages}")

sent_messages = []
messages = ["hey when is the party???", "i think i might sleep instead",
"its at 11!", "you promised you'd come!", "oh dang, fine!"]

show_messages(messages, sent_messages)
