# Computes square number of N recursively, without multiplication.

## Problem: We want to know N^2 without doing N*N.

### Axiom 1: Square of 0 is 0 (zero product property).
### Axiom 2: Square of 1 is 1. (as 1 is the identity for multiplication).
### Axiom 3: Square of -1 is 1. (as negative multiplied by negative is positive).
### Axiom 4: Square of (N+1) = N^2 + 2N + 1 (the quadratic polynomial formula).

Knowing from Quadratic Formula that (N+1)^2 = N^2 + 2N + 1,
let's call X=N+1 and Y=N. We have then:
    X^2 = Y^2 + 2Y + 1

Another way to see it is by looking at the delta of two consecutive square numbers:
(N+1)^2 - N^2 = N^2 +2N +1 - N^2 => 2N + 1

So 2N + 1 is the arithmetic series of odd numbers.

So as an example, 3**2 (9) is 2**2 (4) + 2*2 + 1 (5) == 9. This is easy.

The interesting bit is that for N=3, the delta of {9} (N^2) - {4} (N-1)^2 == 5 (2N+1) ...
But if we are on (N-1), then the formula is: 2(N-1)+1 -> 2N -2 + 1 -> 2N-1, which means we can compute the delta we need for N when we are computing the square number of (N-1). We can just use 2N-1 when on (N-1) to pre-compute that delta when we are computing the square number of (N-1).  So the arithmetic progression is:
          N:    1  2  3  4  5   6   7   8   9  10
Progression:    1, 3, 5, 7, 9, 11, 13, 15, 17, 19

Therefore, for a given number N, the progression is (2*N)-1, or in other words, 2*(N-1) + 1.
(i.e. 1 + 2+2+...+2 n-1 times).

So we see that for each number N, its power of 2 will be the power of two of the previous number, plus a constant (always a factor of 2).

And the square of each number is always the progression, plus the previous number squared, recursively as follows:
    Progression(N) = Progression(N-1) + 2 => (N*2-1)
         Square(N) = Progression(N) + Square(N-1), for every N.
NOTE: As we will be using recursion and we want to avoid multiplications, we will assume N>=0.

N                 Prog    Square  Result
.
.
-2           =      -5,  (-5 + 9)  {  4}
-1           =      -3,  (-3 + 4)  {  1}
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
10           =      19,  (19 + 81) {100}
 .
 .
 .
etc

In this script we have a few methods to compute the above, as follows:
1) How to compute square numbers of a number, with recursion and the properties
   of the square numbers of the previous number
   (i.e. we compute N**2 by computing (N-1)**2 recursively, and adding the "delta" or "progression number" we pre-computed)
2) Using recursion with memoization
3) Using tail recursion, with memoization
4) And using function decorators to decorate the non-memoized tail recursion,
with memoization.
