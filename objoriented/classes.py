
# Classes

# multiple inheritance possible
# derived class can override any base class method
# classes are created at runtime

# built-in types can be used as base classes for extension by the user

# class members are PUBLIC by default
# member functions are VIRTUAL by default



# Pseudo Pointers

# Multiple names can be bound to the same object, aka aliasing in other
# languages. With mutable objects, aliases behave like pointers in some
# respects.

# Passing an object is cheap since only a pointer is passed by the
# implementation; and if a function modifies an object passed as an
# argument, the caller will see the change — this eliminates the need
# for two different argument passing mechanisms as in Pascal.

# "the caller will see the change" - ?



# Namespaces

# a namespace is a mapping from names to objects

# they are implemented as dictionaries in python

# there is no relation between names in different namespaces!
# eg 2 modules may define maximise() - no confusion since python
# requires to prefix by module name

# the namespace containing all built-in names is created when python
# interpreter starts up, and is never deleted

# a module's namespace is created when module is imported, and is
# usually deleted when interpreter quits.

# namespace examples: built-in variable names, variable names local to
# a module, variable names local to the body of a function



# Inheritance

# syntax for declaration
class Subclass(BaseClass):


    
# Class methods vs Instance methods
# http://www.pythoncentral.io/difference-between-staticmethod-and-classmethod-in-python/

def getNumberOfInstances(className):    # argument isn't a class object aka instance, but a class
    return className.no_inst

class Kls(object):
    no_inst = 0                         # notice no self prefix! this isn't an attribute or field
 
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1   # notice this is not a field, not an attribute! not self.no_inst, but Kls.no_inst


obj = Kls()
obj2 = Kls()
print getNumberOfInstances(Kls)         # 2 will be printed

# not very elegant to have getNumberOfInstances() defined outside class def, so instead can do this:
class Kls(object):
    no_inst = 0
 
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1

    @classmethod
    def getNumberOfInstances(className):
        return className.no_inst


obj = Kls()
print obj.getNumberOfInstances()        # 1 will be printed
print Kls.getNumberOfInstances()        # 1 will be printed

# python (unrigorous) flexibility: whether we call the method from the instance or the class, it passes the class as first argument

