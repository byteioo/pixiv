# coding=utf-8
import json
import re
def isJson(str):
    try:
        json_object = json.loads(str)
    except Exception as e:
        return False
    return True

def deleteSpecialChar(str):
    return re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", str)

