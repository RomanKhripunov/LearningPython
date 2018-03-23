import xml.etree.ElementTree as ET
import os.path as path


xml_file_name = 'country_data.xml'

tree = ET.parse(path.join(xml_file_name))
root = tree.getroot()

print(root.tag)
print(root.attrib)
