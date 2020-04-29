#!/bin/env python3
"""Test recursive square algorithm implementation."""
import unittest
from recursive_square import iterative_square, recursive_square, recursive_square_tail

class SquareTestCommon():
    def setUp(self):
        self.range_start = -100
        self.range_end = 100 + 1
        self.function = None

    def test(self):
        self.assertIsNotNone(self.function)
        #print('{:>4} --> {:>4} {:>4} {:>4}'.format('N', 'BP', 'FP', 'Square'))
        for N in range(self.range_start, self.range_end):
            with self.subTest(N=N):
                bwd_prog, fwd_prog, computed_N = self.function(N)
                #print('{:>4} --> {:>4} {:>4} {:>4}'.format(N, bwd_prog, fwd_prog, computed_N))
                self.assertEqual(computed_N, N**2)


class RecursiveSquareTest(unittest.TestCase, SquareTestCommon):
    def setUp(self):
        SquareTestCommon.setUp(self)
        self.function = recursive_square


class RecursiveSquareTailTest(unittest.TestCase, SquareTestCommon):
    def setUp(self):
        SquareTestCommon.setUp(self)
        self.function = recursive_square_tail


class IterativeSquareTest(unittest.TestCase, SquareTestCommon):
    def setUp(self):
        SquareTestCommon.setUp(self)
        self.function = iterative_square


if __name__ == '__main__':
    unittest.main()
