from random import *
from lang.lang_translate import *

def hello_msg():
    msg_hello_alt_list = lang_obj_fr_fr['hello_alt'] 

    return msg_hello_alt_list[randint(0, len(msg_hello_alt_list) - 1)]