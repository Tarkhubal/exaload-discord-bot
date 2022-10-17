from random import *
from commands.lang.lang_translate import *

def bye_msg():
    msg_bye_alt_list = lang_obj_fr_fr['bye_alt']

    return msg_bye_alt_list[randint(0, len(msg_bye_alt_list) - 1)]
