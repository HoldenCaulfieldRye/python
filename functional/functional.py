# http://docs.python.org/2/howto/functional.html


################################################################################
#               ITERATORS                                                      #
################################################################################

# important foundation for functional-style programs: iterators

# iter() takes any object and tries to return an iterator on it
>>> data = 7,7,6,5,2,1,4,6,7,4,2
>>> it = iter(it)
>>> it
<tupleiterator object at 0x13ec4d0>
>>> it.next()
9
>>> it.next()
4

# use iterators for (exact) sequence unpacking
>>> data = 8,4,32,5
>>> a,b,c,d = iter(data)
>>> a
8
>>> d
5
>>> e,f,g = iter(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack

# common operations on an iterator's output:
# 1) Generator expression: performs an operation for every element
# 2) List comprehension: selects a subset of elements that meet some condition

# Generator expression - always surrounded by ()
# eg define an iterator that skips whitespace, using predefined line.strip()
>>> list = '   i', ' want', '   to', ' join', ' ef', 'and', '   launch'
>>> stripped_iter = (string.strip() for string in list)              # notice '()' syntax
>>> stripped_iter.next()                                             # notice nothing to def
'i'
>>> stripped_iter.next()
'want'
>>> stripped_iter.next()
'to'

# List comprehension - always surrounded by []
# eg define a list that is another list stripped of its whitespace
>>> stripList = [word.strip() for word in list]                      # notice '[]' syntax
>>> stripList                                                        # notice nothing to def
['i', 'want', 'to', 'join', 'ef', 'and', 'launch', 'my', 'startup']

# multiple for...in clauses
# cartesian product
>>> seq1 = ['cat', 'dog']
>>> seq2 = ['white', 'black']
>>> seq = [(x,y) for x in seq1 for y in seq2]                        # notice tuple needs '()'
>>> seq
[('cat', 'white'), ('cat', 'black'), ('dog', 'white'), ('dog', 'black')]



# CHECK OUT this LAMBDA FUNCTIONS TUTORIAL
# this will make you a badass
# http://www.secnetix.de/~olli/Python/lambda_functions.hawk
