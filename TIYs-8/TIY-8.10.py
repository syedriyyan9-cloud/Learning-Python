# Date: 13 november 2025
# Name: Riyyan

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

def send_messages(messages, sent_messages):
    '''moves the values of messages to sent messages and prints them one by one'''
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
        print(current_message)

text_messages = ["what's up","how are ya doing","left on read"]
sent_messages = []

send_messages(text_messages, sent_messages)

print(text_messages)
print(sent_messages)