import ObjToXML
import ObjToJSON

# Define sample class
class TestClass:
    def __init__(self, c, d):
        self.TestClass_1 = c
        self.TestClass_2 = d
class TestClassInside:
    def __init__(self, c, d):
        self.TestClassInside_1 = c
        self.TestClassInside_2 = d

class TestClassInsideInside:
    def __init__(self, c, d):
        self.TestClassInsideInside_1 = c
        self.TestClassInsideInside_2 = d

# Creating object
xx = TestClassInsideInside("5T","6T")
yy = TestClassInsideInside("5A","6A")
zz = TestClassInsideInside("5B","6B")
x = TestClassInside("5T", (xx, yy, zz))
v = TestClass(4, x)
# convert to xml
print(ObjToXML.format_to_xml(v))

# Creating object
xx = TestClassInsideInside("5T","6T")
yy = TestClassInsideInside("5A","6A")
zz = TestClassInsideInside("5B","6B")
x = TestClassInside(3, (xx, yy, zz))
v = TestClass(4, x)
# convert to Json
print(ObjToJSON.format_to_json(v))

