from random import *
def hello_msg():
    msg_hello_alt_list = ['Hello ! ✌', 'Hi !!', 'Hey !', 'Hi ! :3']
    
    return msg_hello_alt_list[randint(0, len(msg_hello_alt_list) - 1)]