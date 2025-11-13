# Date: 13 november 2025
# Name: Riyyan

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.

def send_messages(messages, sent_messages):
    '''moves the values of messages to sent messages and prints them one by one'''
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
        print(current_message)

text_messages = ["what's up","how are ya doing","left on read"]
sent_messages = []

send_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)