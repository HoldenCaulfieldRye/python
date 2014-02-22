# The Element Tree XML API
# http://docs.python.org/2/library/xml.etree.elementtree.html


# PART 1: ACCESSING XML ELEMENTS


country         |  rank  | year  | GPD/capita |
----------------+--------+-------+------------+
Liechtenstein   |   1    | 2008  |  141,000   |
Singapore       |   4    | 2011  |   59,900   |
Panama          |   68   | 2011  |   13,600   |
----------------------------------------------+

root[0].tag            |root[0][0].tag  |root[0][1].tag  |root[0][2].tag  |
-----------------------+----------------+----------------+----------------+
root[0].attrib['name'] |root[0][0].text |root[0][1].text |root[0][2].text |
root[1].attrib['name'] |root[1][0].text |root[1][1].text |root[1][2].text |
root[2].attrib['name'] |root[2][0].text |root[2][1].text |root[2][2].text |
--------------------------------------------------------------------------+


# Root: contains all data
# Element.text:   a piece of parsed xml code
# Element.tag:    attribute name
# Element.attrib: general purpose dict
>>> root[0].attrib.keys()
['name']                   # seems a bit hacky
>>> root.attrib.keys()
[]


# Import data
import xml.etree.ElementTree as ET
tree = ET.parse('example.xml')
root = tree.getroot()






# Child nodes are nested


# example xml:
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>     # direction?
        <neighbor name="Switzerland" direction="W"/> # how represented in table?
    </country>                                       # dunno so left it out
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
