#!/usr/bin/env python3
"""Computes square number of N recursively, without any multiplications."""
from functools import wraps


def static_vars(**kwargs):
    """Add static variables to functions."""
    def wrap(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return wrap


def memoization_decorator(func):
    """Add simple memoization to a function."""
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        number = args[0]
        if number in func.square_cache.keys():
            return func.square_cache[number]
        square = func(*args, **kwargs)
        func.square_cache[number] = square
        return square
    return wrapper_decorator


@memoization_decorator
@static_vars(square_cache={0: (-1, 1, 0)})
def recursive_square(number):
    """Compute the square of N as described by the recursive algorithm."""
    if number < 0:
        bwd_prog, fwd_prog, square = recursive_square(-number)
        return (-bwd_prog, -fwd_prog, square)
    if number == 0:
        return (-1, 1, 0)
    n_minus1_bwd_prog, n_minus1_fwd_prog, n_minus1_square = recursive_square(number - 1)
    n_bwd_prog = n_minus1_bwd_prog + 2
    n_fwd_prog = n_minus1_fwd_prog + 2
    n_square = n_minus1_square + n_minus1_fwd_prog
    result = (n_bwd_prog, n_fwd_prog, n_square)
    return result


@memoization_decorator
@static_vars(square_cache={0: (-1, 1, 0)})
def recursive_square_tail(number):
    """Compute tail recursive square of N."""
    def recursive_square_tail_full(number, idx, bprog, fprog, square):
        if number < 0:
            bwd_prog, fwd_prog, square = recursive_square_tail(-number)
            return (-bwd_prog, -fwd_prog, square)

        ## small optimization
        if idx not in recursive_square_tail.square_cache.keys():
            recursive_square_tail.square_cache[idx] = (bprog, fprog, square)

        if number == 0:
            return (bprog, fprog, square)
        return recursive_square_tail_full(number - 1,
                                          idx + 1,
                                          bprog + 2,
                                          fprog + 2,
                                          square + bprog + 2)

    ## Another small optimization. If we already have the previous number,
    ## just use it using the fwd progression available
    if number - 1 in recursive_square_tail.square_cache.keys():
        bwd_prog, fwd_prog, square = recursive_square_tail.square_cache[number - 1]
        if number < 0:
            return (bwd_prog + 2, fwd_prog + 2, square + bwd_prog)
        return (bwd_prog + 2, fwd_prog + 2, square + fwd_prog)

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
    count = number-1
    while count >= 0:
        square += fwd_prog
        bwd_prog += 2
        fwd_prog += 2
        count -= 1
    if negative:
        return (-bwd_prog, -fwd_prog, square)
    return (bwd_prog, fwd_prog, square)
