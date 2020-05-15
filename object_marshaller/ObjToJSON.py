from __future__ import (absolute_import, division, print_function)
from io import StringIO
import config

primitive = (int, float, str, bool)
lists = (list, tuple, set, dict)

def is_primitive(thing):
        return isinstance(thing, primitive)

def is_lists(thing):
        return isinstance(thing, lists)

def format_to_json(v):
    config.jsonStr = StringIO()
    config.jsonStr.write('{ "' + v.__class__.__name__ + '": {')
    print_instance_attributes(v, "\t")
    performLastElement()
    config.jsonStr.write('} }')
    json = config.jsonStr.getvalue()
    config.jsonStr.close()
    return json

def performLastElement():
    if config.jsonStr.getvalue()[-1] == ',':
        str = config.jsonStr.getvalue()[:-1]
        config.jsonStr = StringIO()
        config.jsonStr.write(str)

def print_instance_attributes(v, tab):
    #   print('[instance attributes]')
    for attribute, value in v.__dict__.items():
        if is_primitive(value):
            config.jsonStr.write("\n" + tab + '"' + attribute + '": "' + str(value) + '",')
        elif is_lists(value):
            config.jsonStr.write("\n" + tab + '"' + attribute + '": [')
            for i in value:
                if is_primitive(i):
                    config.jsonStr.write(str(i) + ",")
                else:
                    config.jsonStr.write("\n" + tab + '{')
                    print_instance_attributes(i, tab + tab)
                    performLastElement()
                    config.jsonStr.write("\n" + tab + '},')
            performLastElement()
            config.jsonStr.write( ']' + ',')
        else:
            config.jsonStr.write("\n" + tab + '"' + attribute + '": {')
            print_instance_attributes(value, tab + tab)
            performLastElement()
            config.jsonStr.write("\n" + tab + '}')
