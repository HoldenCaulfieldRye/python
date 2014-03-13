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

        
# Element() and SubElement()
>>> ET.Element('Poland')
<Element 'Poland' at 0x7f0b8fc5ba10>

>>> ET.dump(tree)
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
<Poland /></data>

