"""
fibonacci

functions to compute fibonacci numbers

Complete problems 2 and 3 in this file.
"""

import time # to compute runtimes
from tqdm import tqdm # progress bar

# Question 2
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    pass


# Question 2
def fibonacci_iter(n):
    if n == 0:
        return 0
    a=0
    b=1
    while n-1>0:
        a,b = b, a+b
        n-=1
    return b
    pass

print("The first 30 fibonacci numbers using fibonacci_recursive is: ")
for i in range(0,30):
    print(fibonacci_recursive(i))

print("The first 30 fibonacci numbers using fibonacci_iter is: ")
for i in range(0,30):
    print(fibonacci_iter(i))

import numpy as np
# Question 3
def fibonacci_power(n):
    # The matrix A and vector x_1 are given and can be defined in NumPy arrays.
    A = np.array([[1,1],[1,0]])
    x_1 = np.array([1,0])
    # We define what F_0 should be, which is 0.
    if n == 0:
        return 0
    else:
        def power(mat, i):
            def isodd(i):
                """
                returns True if n is odd
                """
                return i & 0x1 == 1
            if i == 0:
                # when n=1, the output should be just x_1
                return np.identity(2)
            if isodd(i):
                return power(mat@mat, i//2)@mat
            else:
                return power(mat@mat, i//2)
        x_n = power(A,n-1)@x_1
        # we need just the first element of x_n
        return int(x_n[0])

for i in range(0,30):
    print(fibonacci_power(i))

if __name__ == '__main__':
    """
    this section of the code only executes when
    this file is run as a script.
    """
    def get_runtimes(ns, f):
        """
        get runtimes for fibonacci(n)

        e.g.
        trecursive = get_runtimes(range(30), fibonacci_recusive)
        will get the time to compute each fibonacci number up to 29
        using fibonacci_recursive
        """
        ts = []
        for n in tqdm(ns):
            t0 = time.time()
            fn = f(n)
            t1 = time.time()
            ts.append(t1 - t0)

        return ts


    nrecursive = range(35)
    trecursive = get_runtimes(nrecursive, fibonacci_recursive)

    niter = range(10000)
    titer = get_runtimes(niter, fibonacci_iter)

    npower = range(10000)
    tpower = get_runtimes(npower, fibonacci_power)

    ## write your code for problem 4 below...

import matplotlib.pyplot as plt
plt.loglog(nrecursive,trecursive, label=f"Recursive")
plt.loglog(niter,titer, label=f"Iteration")
plt.loglog(npower,tpower, label=f"Power")
plt.legend()
plt.xlabel("n")
plt.ylabel("run time")
plt.title("Fibonacci Algorithm Run Times (log-log)")
plt.show()
plt.savefig('Fibonacci_runtime.png')
