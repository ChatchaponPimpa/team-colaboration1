import re
import long_responses as long

def get_response(user_input):
    split_message = re.split(r'\s+l[,;?!.-]\s-*',user_input.lower())

# Testing the response system
while True:
    print("Bot:" + get_response(input("You":)))