# The Element Tree XML API
# http://docs.python.org/2/library/xml.etree.elementtree.html


# PART 2: MODIFYING XML ELEMENTS

country         |  rank  | year  | GPD/capita |
----------------+--------+-------+------------+
Liechtenstein   |   1    | 2008  |  141,000   |
Singapore       |   4    | 2011  |   59,900   |
Panama          |   68   | 2011  |   13,600   |
----------------------------------------------+

import xml.etree.ElementTree as ET
tree = ET.parse('example.xml')
root = tree.getroot()


# Modify an attribute in all tuples
# eg rank attribute
for entry in root.iter('rank'):
    newValue = int(entry.text) + 1  # hacky! no int field
    entry.text = str(newValue)      # modifying text ie string
    entry.set('updated', 'yes')     # so hacky!


# Remove tuples
# eg all tuples with rank > 50
for _tuple in root.findall('country'): # for all _tuples; find via key
    if int(_tuple.find('rank').text) > 50: # criterion
        root.remove(_tuple)


# Add tuples
>>> a = ET.Element('a')
>>> b = ET.SubElement(a, 'b')
>>> c = ET.SubElement(a, 'c')
>>> d = ET.SubElement(c, 'd')
>>> ET.dump(a)
<a><b /><c><d /></c></a>

        
