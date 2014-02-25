# Fibonacci numbers module

def fib(n):
    """Return n-th element of fibonacci sequence."""
    a, b, count = 0, 1, 1
    if n == 0:
        return a
    while count < n:
        a, b, count = b, a+b, count+1 # notice no need for temp!
    return b
        
