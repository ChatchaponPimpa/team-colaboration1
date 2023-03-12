import re
import long_responses as long

daf message_probab

def get_response(user_input):
    split_message = re.split(r'\s+l[,;?!.-]\s-*',user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))