# Modules - file containing Python definitions and standalone statements

# module_name can be wtv; filename is module_name.py

# within module, module_name (as a string) is available as the value
# of the global variable __name__ .

# use your favorite text editor to create a file called fibo.py in the
# current directory with 'Fibonacci numbers module' as 1st line comment

# then import module in console
>>> import fibo

# cannot directly access functions defined in module!
# module is an object, its functions are its member functions
>>> import fibo
>>> for i in range(20):
...     print fibo.fib(i)  # see here
... 
0
1
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584

# for comfort you can assign local names to member functions
>>> fib = fibo.fib
>>> fib(83)
61305790721611591


# Standalone Statements
# intended to initialise the module
# or to be used as executable script


# Module Stackframes
# each module has its own private value table aka stackframe, used as
# a local symbol table by all functions defined in the module. 
# so variable names local to the module won't clash with variable names
# local to space in which module is called.

# "if you know what you are doing you can touch a module’s global
#  variables with the same notation used to refer to its functions,
#  modname.itemname" - ?

# modules can import other modules
# use 'from' to import names from a module directly into the importing
# module’s symbol table
# ie import locally
>>> fib = range
>>> fib(3)
[0, 1, 2]
>>> from fibo import fib
>>> fib(5)
3

# import whole module locally
>>> from fibo import *
# but refrain because makes code poorly readable
# reader doesn't know which you imported, and since functions will now
# be local, reader won't know which come from the module and which don't

# if on console, and you modify a module, need to reload it
>>> reload(fibo)



# Executing Modules as Scripts

# when you run a python module with
>>> python fibo.py <arguments>
# this executes your module and assigns "__main__" to __name__ .

# (recall __name__ is a global string variable which usually holds
#  module_name)

# if at the end of your module, you have:
if __name__ = "__main__":
    # some code
    # ...
    # end of some code

# then the statements will be executed as script

# for example:
if __name__ = "__main__":
    import sys
    fib(int(sys.argv[1]))
# this script imports the sys module, and returns fib(<argument[1]>)
# the if statement can kind of be seen as the main function
# by the way, sys contains everything you enter in console, including
# <arguments>, which is assigned to argv (which is a list?).

# notice this allows you to use the file as an importable module, and
# as executable script



# Module Search Path

# when a module called module_name is imported, the interpreter
# searches for a built-in module with that name.

# if not found, it then searches for module_name.py in directories
# whose addresses are held in the list sys.path

# sys.path is initialised from:
# - directory containing the script
# - current directory
# - PYTHONPATH, a predefined list of directory names
# - the installation-dependent default

# note that the directory containing the script is placed in first
# position, so scripts in that directory will be loaded instead of any
# modules with same name anywhere else (including the python library
# directory).



# Byte-compiling

# module_name.pyc is the byte-compiled version of module_name.py
# module_name.pyo is the optimised version of module_name.pyo

# the only thing that's faster about .pyc or .pyo is the speed at
# which they are loaded. the program doesn't run any faster.

# .pyc files contain the byte-representation of the non-comment text
# in the .py file

# only difference between .pyo and .pyc is that assert statements are
# removed

# the .pyc is generated when module_name is imported for the
# first time, or when the .py has been modified since last time the
# .pyc was generated

# .pyo is generated when python interpreter is invoked with -O flag



# The dir() function

# dir() returns names defined locally
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'numpy']

# dir(module_name) returns sorted list of names defined in module_name
>>> import numpy
>>> dir(numpy)
['ALLOW_THREADS', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_DEFAULT2', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'PackageLoader', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', # ...



 
# Packages

# ...

