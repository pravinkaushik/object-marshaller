from object_marshaller import ObjToXML, ObjToJSON

# Define sample class
class TestClass:<br />
    def __init__(self, c, d):<br />
        self.TestClass_1 = c<br />
        self.TestClass_2 = d<br />
class TestClassInside:<br />
    def __init__(self, c, d):<br />
        self.TestClassInside_1 = c<br />
        self.TestClassInside_2 = d<br />
<br />
class TestClassInsideInside:<br />
    def __init__(self, c, d):<br />
        self.TestClassInsideInside_1 = c<br />
        self.TestClassInsideInside_2 = d<br />
<br />
# Creating object for xml<br />
xx = TestClassInsideInside("5T","6T")<br />
yy = TestClassInsideInside("5A","6A")<br />
zz = TestClassInsideInside("5B","6B")<br />
x = TestClassInside("5T", (xx, yy, zz))<br />
v = TestClass(4, x)<br />
# convert to xml<br />
print(ObjToXML.format_to_xml(v))<br />
<br />
# Creating object for json<br />
xx = TestClassInsideInside("5T","6T")<br />
yy = TestClassInsideInside("5A","6A")<br />
zz = TestClassInsideInside("5B","6B")<br />
x = TestClassInside(3, (xx, yy, zz))<br />
v = TestClass(4, x)<br />
# convert to Json<br />
print(ObjToJSON.format_to_json(v))<br />
