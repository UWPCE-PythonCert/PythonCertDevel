#!/usr/bin/env python

import os
import sys
import multiprocessing

from integrate.integrate import integrate, f
# from integrate.integrate import f, integrate_numpy as integrate
from decorators import timer


@timer
def multi_integrate(f, a, b, N, process_count=2):
    """break work into N chunks"""
    N_chunk = int(float(N) / process_count)
    dx = float(b - a) / process_count

    # now using a multiprocessing queue
    results = multiprocessing.Queue()

    def worker(*args):
        results.put(integrate(*args))

    for i in range(process_count):
        x0 = dx * i
        x1 = x0 + dx
        # thread = threading.Thread(target=worker, args=(f, x0, x1, N_chunk))
        process = multiprocessing.Process(target=worker, args=(f, x0, x1, N_chunk))
        process.start()
        print("process %s started" % process.name)

    return sum((results.get() for i in range(process_count)))


if __name__ == "__main__":
    # parameters of the integration
    a = 0.0
    b = 10.0
    N = 10**7
    process_count = 1

    print("Numerical solution with N=%(N)d : %(x)f" %
          {'N': N, 'x': multi_integrate(f, a, b, N, process_count=process_count)})

