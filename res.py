import random

def handle_res(s) -> str:
    lower_message = s.lower()
    
    if lower_message == 'hi':
        return 'Hey there! :)'
    
    if lower_message == 'help': 
        return "help"
    else:
        return " "