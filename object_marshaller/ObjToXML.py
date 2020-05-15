from __future__ import (absolute_import, division, print_function)
from io import StringIO
import config

primitive = (int, float, str, bool)
lists = (list, tuple, set, dict)

def is_primitive(thing):
        return isinstance(thing, primitive)

def is_lists(thing):
        return isinstance(thing, lists)

def format_to_xml(v):
    config.xmlStr = StringIO()
    config.xmlStr.write('<' + v.__class__.__name__ + '>' + '\n')
    print_instance_attributes(v, "\t")
    config.xmlStr.write('<' + v.__class__.__name__ + '/>' + '\n')
    xml = config.xmlStr.getvalue()
    config.xmlStr.close()
    return xml


def print_instance_attributes(v, tab):
    #   config.xmlStr.write('[instance attributes]')
    for attribute, value in v.__dict__.items():
        if is_primitive(value):
            config.xmlStr.write(tab + '<' + attribute + '>' + str(value) + ' <' + attribute + '/>' + '\n')
        elif is_lists(value):
            for i in value:
                config.xmlStr.write(tab + '<' + attribute + '>' + '\n')
                print_instance_attributes(i, tab + tab)
                config.xmlStr.write(tab + '<' + attribute + '/>' + '\n')
        else:
            config.xmlStr.write(tab + '<' + attribute + '>' + '\n')
            print_instance_attributes(value, tab + tab)
            config.xmlStr.write(tab + '<' + attribute + '/>' + '\n')
