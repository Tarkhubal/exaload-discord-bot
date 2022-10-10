from json import *


lang = "fr_fr"

lang_fr_fr = open("commands/lang/fr_fr.json", "r")
lang_fr_fr_content = lang_fr_fr.read()
lang_obj_fr_fr = loads(lang_fr_fr_content)