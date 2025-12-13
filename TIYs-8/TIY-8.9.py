# Date: 13 november 2025
# Name: Riyyan

# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    '''prints elements of a list'''
    for message in messages:
        print(message)

text_messages = ["what's up","how are ya doing","left on read"]

show_messages(text_messages)