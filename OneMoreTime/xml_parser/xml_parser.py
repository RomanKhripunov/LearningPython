import xml.etree.ElementTree as ET
import os.path as path


PATH_TO_XML_FILE = "/Users/r_khripunov/Desktop"
XML_FILE_NAME = 'bw.xml'
RU_REALM = "RU"

tree = ET.parse(path.join(PATH_TO_XML_FILE, XML_FILE_NAME))
root = tree.getroot()

wg_tag = root.find("wg")

# for tag in wg_tag:
#     print(tag.tag)

# realm_tag = wg_tag.find("realm")
# if realm_tag:
#     if realm_tag.text.upper() != RU_REALM:
#         realm_tag.text = RU_REALM
#         tree.write(path.join(PATH_TO_XML_FILE, XML_FILE_NAME))
# else:
#     realm_tag = ET.SubElement(wg_tag, "realm")
#     realm_tag.text = RU_REALM
#     tree.write(path.join(PATH_TO_XML_FILE, XML_FILE_NAME))

print(tree.find("realm"))
