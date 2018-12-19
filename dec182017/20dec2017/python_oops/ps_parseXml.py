# Traverse XML file

import xml.etree.ElementTree as et

doc = et.parse('tmp.xml')
print(doc)
print()

root_tag = doc.getroot()
print(root_tag)
print()
print('tag_name :', root_tag.tag)
print()
print()

for dir_tag in doc.getroot(): #doc.getiterator('directory'): --> It will give directory of all level
    name = dir_tag.tag
    print(name, dir_tag.get('name'))
