#!/usr/bin/env python3
"""Computes square number of N recursively, without any multiplications."""
from functools import wraps


def static_vars(**kwargs):
    """ Decorator to add static variables to functions. """
    # print("static_vars", kwargs)
    def wrap(func):
        # print("inside static_vars.wrap")
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return wrap


def memoization_decorator(func):
    """Add simple memoization to a function."""
    # print("memoization_decorator")
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        number = args[0]
        if number in func.square_cache.keys():
            return func.square_cache[number]
        # print("%s: memoized %s"%(__name__, number))
        square = func(*args, **kwargs)
        func.square_cache[number] = square
        return square
    return wrapper_decorator


@memoization_decorator
@static_vars(square_cache={0: (-1, 1, 0)})
def recursive_square(number):
    # print("recursive_square")
    """Compute the square of N as described by the recursive algorithm."""
    if number < 0:
        bwd_prog, fwd_prog, square = recursive_square(-number)
        return (-fwd_prog, -bwd_prog, square)
    if number == 0:
        return (-1, 1, 0)
    n_minus1_bwd_prog, n_minus1_fwd_prog, n_minus1_square = recursive_square(number - 1)
    n_bwd_prog = n_minus1_bwd_prog + 2
    n_fwd_prog = n_minus1_fwd_prog + 2
    n_square = n_minus1_fwd_prog + n_minus1_square
    result = (n_bwd_prog, n_fwd_prog, n_square)
    # print("recursive", number, result)
    return result


@memoization_decorator
@static_vars(square_cache={0: (-1, 1, 0)})
def recursive_square_tail(number):
    """Compute tail recursive square of N."""
    # print("---> recursive square tail", number)

    # Another small optimization. If we already have the previous number,
    # just use it using the fwd progression available
    if number - 1 in recursive_square_tail.square_cache.keys():
        bwd_prog, fwd_prog, square = recursive_square_tail.square_cache[number - 1]
        return (bwd_prog + 2, fwd_prog + 2, square + fwd_prog)

    def recursive_square_tail_full(number, idx, bprog, fprog, square):
        # print('rsqt: ', number, idx, bprog, fprog, square)
        if number < 0:
            bwd_prog, fwd_prog, square = recursive_square_tail(-number)
            return (-bwd_prog, -fwd_prog, square)

        # small optimization
        if idx not in recursive_square_tail.square_cache.keys():
            recursive_square_tail.square_cache[idx] = (bprog, fprog, square)
        #     print("    memoized", number, idx, bprog, fprog, square)
        # else:
        #     print("    memoiz", number, idx, bprog, fprog, square)

        # print("    full", number, idx, bprog, fprog, square)
        if number == 0:
            return (bprog, fprog, square)
        return recursive_square_tail_full(number - 1,
                                          idx + 1,
                                          bprog + 2,
                                          fprog + 2,
                                          bprog + square + 2)
    return recursive_square_tail_full(number, 0, -1, 1, 0)


@memoization_decorator
@static_vars(square_cache={0: (-1, 1, 0)})
def iterative_square(number):
    """Compute square of N in a bottom-up approach."""
    negative = False
    if number < 0:
        negative = True
        number = -number
    bwd_prog = -1
    fwd_prog = 1
    square = 0
    for n in range(0, number):
        square += fwd_prog
        bwd_prog += 2
        fwd_prog += 2
    if negative:
        return (-bwd_prog, -fwd_prog, square)
    return (bwd_prog, fwd_prog, square)

import sys
if __name__ == "__main__":
    # print("about to call recursive_square")
    print(3, iterative_square(-3))
    print(3, recursive_square(3))
    print(3, recursive_square_tail(3))
    print(10, recursive_square_tail(10))
    print(9, recursive_square_tail(9))
    print(4, recursive_square_tail(4))
    print(-3, recursive_square_tail(-3))
    print(5, recursive_square_tail(5))
    for num in range(-10, 11, 1):
        print(num, recursive_square_tail(num))
    def doit(forward=True):
        """Compute recursion and tail recursion, and prints results."""
        if forward:
            range_is = range(1,51)
        else:
            range_is = range(50, 0, -1)
        for num in range_is:
            recur = recursive_square(num)
            tail = recursive_square_tail(num)
            iterative = iterative_square(num)
            def compare(label, left, right):
                fmt_short = 'n^2({:^5}) = {:>5}  ... (bwd:{:^5}, fwd:{:^5})'
                fmt_long = '%s       ....     %s' % (fmt_short, fmt_short)
                if left != right:
                    print("NOK",
                          label,
                          fmt_long.format(num, recur[2], recur[0], recur[1],
                                          num, tail[2], tail[0], tail[1]))
                else:
                    print(" OK",
                          label,
                          fmt_short.format(num, recur[2], recur[0], recur[1]))
            compare("recur x      tail", recur, tail)
            compare("recur x iterative", recur, iterative)
    doit()
    doit(False)
    doit()
    doit(False)
