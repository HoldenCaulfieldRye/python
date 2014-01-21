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

# append to list
>>> a += 'mais','bon','c\'est','un','mec','cool'
>>> a
['Miled', 'est', 'un', 'gros', 'caca', 'boudin', 'qui', 'pue', 'mais', 'bon', "c'est", 'un', 'mec', 'cool']

# insert
>>> a.insert(2) = 'un'
>>> a
['Miled', 'est', 'un', 'gros', 'caca', 'boudin']

# remove x specifically
list.remove(x)
# returns error if x not in there

# pop i-th item (ie remove and return it)
list.pop(i)
# returns error if i out of bounds

list.index(x)

list.count(X)

list.sort()

list.reverse()

# can use lists as queues, as stacks


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



# defining a function
# 'def' introduces a function definition
# in brackets is the list of formal parameters, which are alyways called by ref
# body must be indented
# """...""" is the documentation string: user can interactively browse through
# code with it, so good practice ot include one
>>> def fib(n):                      
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print a,
...         a, b = b, a+b
...
# notice fib() has no return statement
# in fact, compiler adds a null return statement if none is given by programmer
# 'null' in python is 'none'

# in this other def, there is a reutrn value
# notice no need to specify return type in opening statement
>>> def fib2(n): # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...

# can specify default values for args
# achieves same thing as overloading!
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint


# positional arguments and keyword arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, " !"

# notice a space at the end of the string is added too
# '--' gets printed but also performs NL


parrot(1000)
# valid call wih one positional argument
# other args take default values

parrot(voltage=1000)
# valid call with one keyword argument
# other args take default values

parrot(voltage=34, action='fly')
# valid call with two keyword arguments

parrot(action='fly', voltage=34)
# valid call with two keyword arguments
# you see, position doesn't matter here


# and now for invalid calls
parrot()
parrot(action='die', 1000) # YEP! positional arguments must go first
parrot(110, voltage=220) # duplicate value for same argument
parrot(110, condition='a stiff') # known keyword argument


# Lambda expressions
def make_incrementor(n):
    return lambda x: x + n


>>> def incrementor(n):
...     return lambda x: x + n
... 
>>> f = incrementor(3)
>>> f(0)
3
>>> f(1)
4


# Docstring or documentation strings
# docstring will be returned after following:
print function.__doc__

# first line should be a short, concise summary of object's purpose.
# no need to state the object's name or type, since you can get these
# via other means.
# line should start with capital letter and end with full stop.


# ---

# 5. Data Structures

# list methods (pasted them by list intro)

# Functional Programming Tools

filter(bool_function, baseList)
# returns list of args of bool_function(element) is true,
# element spanning baseList

map(item_function, baseList)
# returns list of returns of item_function(element),
# element spanning baseList


