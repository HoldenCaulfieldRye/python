# https://pythonhosted.org/joblib/parallel.html

# Parallel is a class to parallelise for-loops using multiprocessing.
# delayed is a function for creating a tuple (function, args, kwargs)
# with a functional (?) syntax

# WOAH! it won't parallelise on a multi-core processor!
# or maybe it can? http://bit.ly/1kSdgBR

# eg:
from math import sqrt
[sqrt(i ** 2) for i in range(10)]
# becomes, for 3 CPU cores:
from joblib import Parallel, delayed
Parallel(n_jobs=3)(delayed(sqrt)(i ** 2) for i in range(10))


# under the hood: Parallel object forks the python interpreter in
# multiple processes to execute each of the items of the list,
# concurrently, on separate cores.
