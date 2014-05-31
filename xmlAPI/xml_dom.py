xml.dom: the Document Object Model API
# bit.ly/1u0Ep8z

dict to saved xml file:
from dict2xml import *
import numpy as np
d = {'labels':np.array([0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],int),'bad_joint':0}
xmlcontents = dict2xml(d)


Document class:
# represents an entire XML document. inherits from Node.
#  
# bit.ly/1u0EOYR

Node class:
# the base class for Document.
# bit.ly/1u0GeCo  
