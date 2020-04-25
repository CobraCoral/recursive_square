# Computes square number of N recursively, without multiplication.

## Problem: We want to know N^2 without doing N*N, or any multiplication for that matter.

## Knowing from Quadratic Formula that:
![equation](http://latex.codecogs.com/png.latex?%28N&plus;1%29%5E2%20%3D%20N%5E2%20&plus;%202N%20&plus;%201)

## If we look at the delta of two consecutive square numbers:
![equation](http://latex.codecogs.com/png.latex?%28N&plus;1%29%5E2%20-%20N%5E2%20%3D%20N%5E2%20&plus;2N%20&plus;1%20-%20N%5E2%20%5CRightarrow%202N%20&plus;%201)

#### We get 2N + 1.  This is the arithmetic series of odd numbers.

If you want to go forward (to the next square), we need the "forward" delta which is our arithmetic series of odd numbers as seen above:
![equation](http://latex.codecogs.com/png.latex?%28N%5E2%29%20-%20%28N-1%29%5E2%20%3D%202N&plus;1)

But if we are going backwards, our "backward" delta for (N-1)^2 will be:
![equation](http://latex.codecogs.com/png.latex?2%28N-1%29&plus;1%20%5Crightarrow%202N%20-2%20&plus;%201%20%5Crightarrow%202N-1)

The idea is to store 2N whenever computing Square(N), and add +1 for the forward delta (if computing Square(N+1)) or decrease with -1 for the backward delta as needed (if computing Square(N-1)).

To be clearer: If N=3, and you want to go "forward" (N+1), you use:
- ![equation](http://latex.codecogs.com/png.latex?Square%283%29%20&plus;%20%7BForwardDelta%7D%283%29%20%5CRightarrow%209%20&plus;%207%20%5CRightarrow%2016%20%5Cequiv%20Square%284%29)

And if N=3, and you want to go "backward" (N-1), you use:
- ![equation](http://latex.codecogs.com/png.latex?Square%283%29%20-%20%7BBackwardDelta%7D%283%29%20%5CRightarrow%209%20-%205%20%5CRightarrow%204%20%5Cequiv%20Square%282%29)

So the arithmetic "forward" progression is then:
|             |||||||||||
| ----------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|          N: |   1|  2|  3| 4 | 5 |  6 |  7 |  8 |  9 | 10 |
|     Square: |   1|  4|  9| 16| 25| 36 | 49 | 64 | 81 | 100 |
|FWD Progression [Sq(N+1) - Sq(N)]: |   3| 5| 7| 9| 11| 13| 15| 17| 19 |21|
|BWD Progression [Sq(N) - Sq(N-1)]: |   1| 3| 5| 7| 9| 11| 13| 15| 17| 19 |

Therefore, for a given number N, the forward progression is 2N+1. i.e. 2+2+...+2 n times + 1.
And the backward progression is 2N-1. i.e. 2+2+2+...+2 n times - 1.

So we see that for each number N, Square(N+1) == Square(N) + FWD Progression(N), and Square(N-1) == Square(N) - BWD Progression(N).

And the square of each number is always the progression, plus the previous number squared, recursively as follows:
- ![equation](http://latex.codecogs.com/png.latex?Progression%28N%29%5Crightarrow%20Progression%28N-1%29&plus;2)
- ![equation](http://latex.codecogs.com/png.latex?Square%28N%29%20%3D%20Square%28N-1%29%20&plus;%20%7BBackwardProgression%7D%28N%29)
OR
- ![equation](http://latex.codecogs.com/png.latex?Square%28N%29%20%3D%20Square%28N-1%29%20&plus;%20%7BForwardProgression%7D%28N-1%29)

It will suffice to focus on cases where n>=0, and use:
- ![equation](http://latex.codecogs.com/png.latex?Square%28n%29%20%3D%20Square%28-n%29%20%7B%5Ctextup%7B%20when%20%7D%7D%20n%3C0)
- ![equation](http://latex.codecogs.com/png.latex?Square%280%29%20%3D%200)
- ![equation](http://latex.codecogs.com/png.latex?%5Cforall%20n%2C%20Square%28n%29%20%3D%20Square%28n-1%29%20&plus;%202n-1%20%5Ctextup%7B%20%28Eq.%201%29%7D)
- ![equation](http://latex.codecogs.com/png.latex?%5Ctextup%7BSo%20if%20%7D%20n%3E0%2C%20Square%28n%29%20%3D%20Square%280%29&plus;%5B2*1-1%5D&plus;%5B2*2-1%5D&plus;...&plus;%5B2*n-1%5D%20%5Ctextup%7B%20%28by%20using%20Eq.%201%20n%20times%29%7D)
- ![equation](http://latex.codecogs.com/png.latex?%5Ctextup%7BThat%20is%2C%20%7D%20Square%28n%29%3D%5B2*1-1%5D&plus;%5B2*2-1%5D&plus;...&plus;%5B2*n-1%5D%3D2*%281&plus;2&plus;...&plus;n%29-n%20%5Ctextup%7B%20%28Eq.%202%29%7D)
- Note that Eq. 2 is consistent with (in fact, a proof of) the well-know fact that ![equation](http://latex.codecogs.com/png.latex?1%20&plus;%202%20&plus;...&plus;%20n%20%3D%20%5Ctfrac%7Bn%28n&plus;1%29%7D%7B2%7D).
\
\
Eq. 1 is the basis for the recursive approach. Eq. 2 for the iterative approach.\
\
Recursive program:
```
Square(n)
if (n<0) return Square(-n)
if (n==0) return (-1, 0)
fwd_progression_n_minus_1, bwd_progression_n_minus_1, square_n_minus_1 = Square(n-1)
bwd_progression_n = bwd_progression_n_minus_1 + 2
fwd_progression_n = fwd_progression_n_minus_1 + 2
square_n = fwd_progression_n_minus_1 + square_n_minus_1
return (fwd_progression_n, square_n)
```

Iterative program:
```
Square(n)
if (n<0) return Square(-n)
if (n==0) return 0
result=-n
for (i from 1 to n)
    result += 2*i
return result
```

#### NOTE: The table below uses the ![equation](http://latex.codecogs.com/png.latex?Square%28N%29%20%3D%20Square%28N-1%29%20&plus;%20%7BForwardProgression%7D%28N-1%29) equation

| N   |          FWD Prog |   Square | Result| Comments |
| :---: | -----------------: | :--------: | :-----: | :-------- |
|.     |                   |          |       |          |
|.     |                   |          |       |          |
|-2    |             -3|  (-5 + 9) | {  4}|              |
|-1    |            -1|  (-3 + 4) | {  1}|              |
| 0    |             1|  (-1 + 1) | {  0}|              |
| 1    |             3|  ( 1 + 0) | {  1}|              |
| 2    |             5|  ( 3 + 1) | {  4}  | 3 is previous Prog (1) + 2|
| 3    |             7|  ( 5 + 4) | {  9}  | 5 is previous Prog (3) + 2|
| 4    |             9|  ( 7 + 9) | { 16}  | 7 is prev. Prog (5) + 2|
| 5    |              11|  ( 9 + 16) |{ 25} |  and so on... |
| 6    |            13|  (11 + 25)| { 36}|              |
| 7    |             15|  (13 + 36)| { 49}|              |
| 8    |             17|  (15 + 49)| { 64}|              |
| 9    |             19|  (17 + 64)| { 81}|              |
|10    |             21|  (19 + 81)| {100}|              |
 |.     |                   |          |       |          |
 |.     |                   |          |       |          |
 |.     |                   |          |       |          |
etc

In this script we have a few methods to compute the above, as follows:
1) How to compute square numbers of a number, with recursion and the properties
   of the square numbers of the previous number
   (i.e. we compute N^2 by computing (N-1)^2 recursively, and adding the "delta" or "progression number" we pre-computed)
2) Using recursion with memoization
3) Using tail recursion, with memoization
4) And using function decorators to decorate the non-memoized tail recursion,
with memoization.
