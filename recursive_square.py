#!/usr/bin/env python3
"""Computes square number of N recursively, without any multiplications."""
import functools


def memoization_decorator(func):
    """Add simple memoization to a function."""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        number = args[0]
        if number in memoization_decorator.dictionary.keys():
            return memoization_decorator.dictionary[number]
        # print("recursive square : memoized", number)
        square = func(*args, **kwargs)
        memoization_decorator.dictionary[number] = square
        return square
    return wrapper_decorator


memoization_decorator.dictionary = {0: (-1, 0)}


@memoization_decorator
def recursive_square(number):
    """Compute the square of N as described by the recursive algorithm."""
    if number < 0:
        prog, square = recursive_square(-number)
        return (-prog, square)
    if number == 0:
        return (-1, 0)
    n_minus1_prog, n_minus1_square = recursive_square(number - 1)
    n_prog = n_minus1_prog + 2
    n_square = n_prog+n_minus1_square
    result = (n_prog, n_square)
    # print("recursive", number, result)
    return result


@memoization_decorator
def recursive_square_tail(number):
    """Compute tail recursive square of N."""
    # print("recursive square tail", number)
    def recursive_square_tail_full(number, prog, square):
        if number < 0:
            prog, square = recursive_square_tail(-number)
            return (-prog, square)
        # print(".... full", number, prog, square)
        if number == 0:
            return (prog, square)
        result = recursive_square_tail_full(number - 1,
                                            prog + 2,
                                            prog + square + 2)
        # print("     tail", number, result)
        return result
    return recursive_square_tail_full(number, -1, 0)

import sys
if __name__ == "__main__":
    print(-3, recursive_square_tail(-3))
    print(5, recursive_square_tail(5))
    for num in range(-10, 11, 1):
        print(num, recursive_square_tail(num))
    sys.exit(0)
    def doit(forward=True):
        """Compute recursion and tail recursion, and prints results."""
        if forward:
            range_is = range(1,51)
        else:
            range_is = range(50, 0, -1)
        for num in range_is:
            recur = recursive_square(num)
            tail = recursive_square_tail(num)
            fmt_short = 'n^2({:^5}) = {:>5}  ... ({:^5})'
            fmt_long = '%s       ....     %s' % (fmt_short, fmt_short)
            if recur != tail:
                print(fmt_long.format(num, recur[1], recur[0],
                                      num, tail[1], tail[0]))
            else:
                print(fmt_short.format(num, recur[1], recur[0]))
    doit()
    doit(False)
    doit()
    doit(False)
