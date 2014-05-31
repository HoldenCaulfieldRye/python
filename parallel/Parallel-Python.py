# documentation:
# http://www.parallelpython.com/content/view/15/30/#API

# examples:
# http://www.parallelpython.com/content/view/17/31/

import pp

# start pp execution with the number of workers set to the number of
# processors in the system
job_server = pp.Server()



# Submit a job of calulating sum_primes(100) for execution. 
# sum_primes - the function
# (100,) - tuple with arguments for sum_primes
# (isprime,) - tuple with functions on which function sum_primes depends
# ("math",) - tuple with module names which must be imported before sum_primes execution
# Execution starts as soon as one of the workers will become available
import math, sys, time, pp
job_server = pp.Server() # Creates jobserver with automatically detected number of workers
job1 = job_server.submit(sum_primes, (100,), (isprime,), ("math",))

def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2,n) if isprime(x)])

def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2: return False
    if n == 2: return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0: return False
        i += 1
    return True
