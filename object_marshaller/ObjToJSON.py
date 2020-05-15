from __future__ import (absolute_import, division, print_function)
from io import StringIO

class JSON_Class:
    def __init__(self, json_str):
        json_str = StringIO()
        
primitive = (int, float, str, bool)
lists = (list, tuple, set, dict)

def is_primitive(thing):
        return isinstance(thing, primitive)

def is_lists(thing):
        return isinstance(thing, lists)

def format_to_json(v):
    JSON_Class.jsonStr = StringIO()
    JSON_Class.jsonStr.write('{ "' + v.__class__.__name__ + '": {')
    print_instance_attributes(v, "\t")
    performLastElement()
    JSON_Class.jsonStr.write('} }')
    json = JSON_Class.jsonStr.getvalue()
    JSON_Class.jsonStr.close()
    return json

def performLastElement():
    if JSON_Class.jsonStr.getvalue()[-1] == ',':
        str = JSON_Class.jsonStr.getvalue()[:-1]
        JSON_Class.jsonStr = StringIO()
        JSON_Class.jsonStr.write(str)

def print_instance_attributes(v, tab):
    #   print('[instance attributes]')
    for attribute, value in v.__dict__.items():
        if is_primitive(value):
            JSON_Class.jsonStr.write("\n" + tab + '"' + attribute + '": "' + str(value) + '",')
        elif is_lists(value):
            JSON_Class.jsonStr.write("\n" + tab + '"' + attribute + '": [')
            for i in value:
                if is_primitive(i):
                    JSON_Class.jsonStr.write(str(i) + ",")
                else:
                    JSON_Class.jsonStr.write("\n" + tab + '{')
                    print_instance_attributes(i, tab + tab)
                    performLastElement()
                    JSON_Class.jsonStr.write("\n" + tab + '},')
            performLastElement()
            JSON_Class.jsonStr.write( ']' + ',')
        else:
            JSON_Class.jsonStr.write("\n" + tab + '"' + attribute + '": {')
            print_instance_attributes(value, tab + tab)
            performLastElement()
            JSON_Class.jsonStr.write("\n" + tab + '}')
