from random import *
def bye_msg():
    msg_bye_alt_list = ['Bye ! 👋', 'Bye !', 'Bye ! :3' 'Goodbye :3']

    return msg_bye_alt_list[randint(0, len(msg_bye_alt_list) - 1)]