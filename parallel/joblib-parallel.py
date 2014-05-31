# https://pythonhosted.org/joblib/parallel.html
# http://bit.ly/1kSdgBR


Parallel:
# a class to parallelise for-loops using multiprocessing.

delayed:
# a function for creating a tuple (function, args, kwargs)
# with a functional (?) syntax

kwargs:
# modules to import?  

example:
from math import sqrt
from joblib import Parallel, delayed
[sqrt(i ** 2) for i in range(10)]
# becomes, for 3 CPU cores:
Parallel(n_jobs=3)(delayed(sqrt)(i ** 2) for i in range(10))

# under the hood: Parallel object forks the python interpreter in
# multiple processes to execute each of the items of the list,
# concurrently, on separate cores.


multi{ threads vs processes }:
# If you know that the function you are calling is based on a compiled extension that releases the Python Global Interpreter Lock (GIL) during most of its computation then it might be more efficient to use threads instead of Python processes as concurrent workers.


parallel IO:
# http://stackoverflow.com/questions/22755218/parallel-i-o-why-does-it-work
# http://stackoverflow.com/questions/23970655/parallelise-an-io-heavy-for-loop-stupid-idea
