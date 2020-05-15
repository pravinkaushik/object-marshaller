from __future__ import (absolute_import, division, print_function)
from io import StringIO

class XML_Class:
    def __init__(self, xml_str):
        xmlStr = StringIO()

primitive = (int, float, str, bool)
lists = (list, tuple, set, dict)

def is_primitive(thing):
        return isinstance(thing, primitive)

def is_lists(thing):
        return isinstance(thing, lists)

def format_to_xml(v):
    XML_Class.xmlStr = StringIO()
    XML_Class.xmlStr.write('<' + v.__class__.__name__ + '>' + '\n')
    print_instance_attributes(v, "\t")
    XML_Class.xmlStr.write('<' + v.__class__.__name__ + '/>' + '\n')
    xml = XML_Class.xmlStr.getvalue()
    XML_Class.xmlStr.close()
    return xml


def print_instance_attributes(v, tab):
    #   xmlStr.write('[instance attributes]')
    for attribute, value in v.__dict__.items():
        if is_primitive(value):
            XML_Class.xmlStr.write(tab + '<' + attribute + '>' + str(value) + ' <' + attribute + '/>' + '\n')
        elif is_lists(value):
            for i in value:
                XML_Class.xmlStr.write(tab + '<' + attribute + '>' + '\n')
                print_instance_attributes(i, tab + tab)
                XML_Class.xmlStr.write(tab + '<' + attribute + '/>' + '\n')
        else:
            XML_Class.xmlStr.write(tab + '<' + attribute + '>' + '\n')
            print_instance_attributes(value, tab + tab)
            XML_Class.xmlStr.write(tab + '<' + attribute + '/>' + '\n')
