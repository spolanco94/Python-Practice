# Using the code from 8-10, call the function 'send_messages' using a copy of
# the list of messages. print both lists to show that there hasn't been a change

def show_messages(messages, sent_messages):
    """Displays a series of text messages"""
    while messages:
        curr = messages.pop()
        print(f"> {curr}")
        sent_messages.append(curr)

    sent_messages.reverse()
    return sent_messages
    # print(f"Messages: {messages}")
    # print(f"Sent messages: {sent_messages}")
    
sent_messages = []
messages = ["hey when is the party???", "i think i might sleep instead", 
"its at 11!", "you promised you'd come!", "oh dang, fine!"]

sent_messages = show_messages(messages[:], sent_messages)

print(f"Messages: {messages}")
print(f"Sent messages: {sent_messages}")