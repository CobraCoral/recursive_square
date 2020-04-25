#!/usr/bin/env python3
"""Computes square number of N recursively, without multiplication.

Problem: We want to know N^2 without doing N*N.

Axiom 1: Square of 0 is 0 (zero product property).
Axiom 2: Square of 1 is 1. (as 1 is the identity for multiplication).
Axiom 3: Square of -1 is 1. (as negative multiplied by negative is positive).
Axiom 4: Square of (N+1) = N^2 + 2N + 1 (the quadratic polynomial formula).

Knowing from Quadratic Formula that (N+1)^2 = N^2 + 2N + 1,
let's call X=N+1 and Y=N. We have then:
    X^2 = Y^2 + 2Y + 1

Another way to see it is by looking at the delta of two consecutive square numbers:
(N+1)^2 - N^2 = N^2 +2N +1 - N^2 => 2N + 1

So 2N + 1 is the arithmetic series of odd numbers.

The deltas of each number follow an this progression of +2 always,
starting at 1 for 1 square.

So the arithmetic progression is:
          N:    1  2  3  4  5   6   7   8   9  10
Progression:    1, 3, 5, 7, 9, 11, 13, 15, 17, 19
Therefore, for a given number N, the progression is (2*N)-1,
or in other words, 2*(N-1) + 1.
(i.e. 1 + 2+2+...+2 n-1 times).

So we see that for each number N, its power of 2 will be the power of two
of the previous number, plus a constant (always a factor of 2).

And the square of each number is always the progression, plus the previous
number squared, recursively as follows:
    Progression(N) = Progression(N-1) + 2 => (N*2-1)
         Square(N) = Progression(N) + Square(N-1), for every N.
NOTE: As we will be using recursion and we want to avoid multiplications, we will assume N>=0.

N                Prog    Square  Result
.
.
-2          =      -5,  (-5 + 9)  {  4}
-1          =      -3,  (-3 + 4)  {  1}
0           =      -1,  (-1 + 1)  {  0}
1           =       1,  ( 1 + 0)  {  1}
2           =       3,  ( 3 + 1)  {  4}  -> 3 is previous Prog (1) + 2
3           =       5,  ( 5 + 4)  {  9}  -> 5 is previous Prog (3) + 2
4           =       7,  ( 7 + 9)  { 16}  -> 7 is prev. Prog (5) + 2
5           =       9,  ( 9 + 16) { 25}  -> and so on...
6           =      11,  (11 + 25) { 36}
7           =      13,  (13 + 36) { 49}
8           =      15,  (15 + 49) { 64}
9           =      17,  (17 + 64) { 81}
10          =      19,  (19 + 81) {100}
.
.
.
etc

In this script we have a few methods to compute the above, as follows:
1) How to compute square numbers of a number, with recursion and the properties
   of the square numbers of the previous number
   (i.e. we compute N**2 by computing (N-1)**2)
2) Using recursion with memoization
3) Using tail recursion, with memoization
4) And using function decorators to decorate the non-memoized tail recursion,
with memoization.
"""
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


memoization_decorator.dictionary = {1: (1, 1)}


@memoization_decorator
def recursive_square(number):
    """Compute the square of N as described by the recursive algorithm."""
    if number < 1:
        print("ERROR: N must be >= 1")
        return (None, None)
    if number == 1:
        return (1, 1)
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
        if number < 1:
            print("ERROR: N must be >= 1")
            return (None, None)
        # print(".... full", number, prog, square)
        if number == 1:
            return (prog, square)
        result = recursive_square_tail_full(number - 1,
                                            prog + 2,
                                            prog + square + 2)
        # print("     tail", number, result)
        return result
    return recursive_square_tail_full(number, 1, 1)


if __name__ == "__main__":
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
