# Make python script executable (from terminal):
chmod +x myscript.py


# no need to specify primitive type, it is inferred automatically
# even better, type conversion is automatic
>>> a /2.0
3.0
>>> a = 5
>>> a += 1
>>> a
6
>>> a / 4.0
1.5


# in interactive mode, last printed expression is assigned to _
# really useful in cases such as these:
>>> tax = 0.12
>>> price = 124
>>> price * tax
14.879999999999999
>>> price - _
109.12
>>> net_of_tax_revenue = _


# strings are concatenated with '+' and repeated with '*'
>>> words = "the United States of "
>>> more_words = words*6
>>> more_words
'the United States of the United States of the United States of the United States of the United States of the United States of '


# subtring of words from x-th to y-th character, y-th not included(!)
words[x:y]
>>> words[5:1]  # can't print backwards; degenerate strings empty by default
''


# string length strlen
len(words)


# lists
# are generic container data type
>>> a = 'je','suis','un','petit','caca','boudin'
>>> a
['je', 'suis', 'un', 'petit', 'caca', 'boudin']

# they are mutable
>>> a[3] = 'gros'
>>> a
['je', 'suis', 'un', 'gros', 'caca', 'boudin']
>>> a[0:3] = 'Miled','est'
>>> a
['Miled', 'est', 'gros', 'caca', 'boudin']

# insert element in list
>>> a.insert(2) = 'un'
>>> a
['Miled', 'est', 'un', 'gros', 'caca', 'boudin']

# append to list
>>> a += 'mais','bon','c\'est','un','mec','cool'
>>> a
['Miled', 'est', 'un', 'gros', 'caca', 'boudin', 'qui', 'pue', 'mais', 'bon', "c'est", 'un', 'mec', 'cool']


# multiple assignment
>>> a, b, c = 9, 4, 1
>>> a
9
>>> b
4
>>> c
1


# elif instead of else if
>>> x = int(raw_input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print 'Negative changed to zero'
... elif x == 0:
...     print 'Zero'
... else:
...     print 'More'
...
More


# any nonzero integer value is true
# a string is true if it is nonempty
# conditions are marked with a colon
# code blocks are marked by indents
# end of code block is marked by NL NL
>>> str = "the United States of"
>>> while str:
...     str = str[1:]
...     print str
... 
he United States of
e United States of
 United States of
United States of
nited States of
ited States of
ted States of
ed States of
d States of
 States of
States of
tates of
ates of
tes of
es of
s of
 of
of
f


# for loop
>>> sentence = 'un','jour','je','serais','le','meilleur','gateur'
>>> for word in sentence:
...     print word
... 
un
jour
je
serais
le
meilleur
gateur
>>> for word in sentence[3:]:
...     print word, len(word)
... 
serais 6
le 2
meilleur 8
gateur 6


# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
>>> class MyEmptyClass:
...     pass
...

