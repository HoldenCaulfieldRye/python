
# Pickle - aka seralize, marshal, flatten

# Unpickle
# step 1: load/open the pickled file
import cPickle as pickle
pickle_file = open(path)
unpickled = pickle.load(pickle_file)

# serialization: process of translating data structures or object state
# into a format that can be stored 
pickle.dump(unpickled, open('pickle_file.wtv', 'wb'))

# converts a python object hierarchy into a byte stream

# unpickling converts a byte stream into an object hierarchy

# converting to byte stream is needed for storing on disk or sending
# over a network

# pickle data format uses a printable ascii representation, so it is
# human-readable with a text editor



# Usage

# to serialize an object hierarchy:
# create a pickler
# call pickler's dump(obj, file, protocol=0) method
# byte stream will be written to file using protocol

# to de-serialize:
# create an unpickler
# call unpickler's load(file) method



# Protocols

# version 0:
# original ascii protocol, python backwards compatible

# version 1:
# old binary format, python backward compatible

# version 2:
# introduced in python-2.3, provides much more efficient pickling of
# new-style classes
# new-style classes: http://docs.python.org/2/glossary.html#term-new-style-class




# cPickle

# written in C, so can be up to 1000 times faster

# does not support subclassing of Pickler and Unpickler classes
# these are implemented as functions

