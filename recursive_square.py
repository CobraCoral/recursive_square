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


memoization_decorator.dictionary = {0: (-1, 1, 0)}


@memoization_decorator
def recursive_square(number):
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


#@memoization_decorator
def recursive_square_tail(number):
    """Compute tail recursive square of N."""
    # print("recursive square tail", number)
    def recursive_square_tail_full(number, idx, bprog, fprog, square):
        # print('rsqt: ', number, idx, bprog, fprog, square)
        if number < 0:
            bwd_prog, fwd_prog, square = recursive_square_tail(-number)
            return (-fwd_prog, -bwd_prog, square)

        # small optimization
        if idx not in memoization_decorator.dictionary.keys():
            memoization_decorator.dictionary[idx] = (bprog, fprog, square)

        # print(".... full", number, idx, bprog, fprog, square)
        if number == 0:
            return (bprog, fprog, square)
        return recursive_square_tail_full(number - 1,
                                          idx + 1,
                                          bprog + 2,
                                          fprog + 2,
                                          bprog + square + 2)
    return recursive_square_tail_full(number, 0, -1, 1, 0)

import sys
if __name__ == "__main__":
    print(3, recursive_square(3))
    print(3, recursive_square_tail(3))
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
            fmt_short = 'n^2({:^5}) = {:>5}  ... (bwd:{:^5}, fwd:{:^5})'
            fmt_long = '%s       ....     %s' % (fmt_short, fmt_short)
            if recur != tail:
                print(fmt_long.format(num, recur[2], recur[0], recur[1],
                                      num, tail[2], tail[0], tail[1]))
            else:
                print(fmt_short.format(num, recur[2], recur[0], recur[1]))
    doit()
    doit(False)
    doit()
    doit(False)
