# Computes square number of N recursively, without multiplication.

## Problem: We want to know N^2 without doing N*N.

### Axiom 1: Square of 0 is 0 (zero product property).
### Axiom 2: Square of 1 is 1. (as 1 is the identity for multiplication).
### Axiom 3: Square of -1 is 1. (as negative multiplied by negative is positive).
### Axiom 4: Square of (N+1) = N^2 + 2N + 1 (the quadratic polynomial formula).

## Knowing from Quadratic Formula that:
![equation](http://latex.codecogs.com/png.latex?%28N&plus;1%29%5E2%20%3D%20N%5E2%20&plus;%202N%20&plus;%201)

## Another way to see it is by looking at the delta of two consecutive square numbers:
![equation](http://latex.codecogs.com/png.latex?%28N&plus;1%29%5E2%20-%20N%5E2%20%3D%20N%5E2%20&plus;2N%20&plus;1%20-%20N%5E2%20%5CRightarrow%202N%20&plus;%201)

#### 2N + 1 is the arithmetic series of odd numbers.

So as an example:
![equation](http://latex.codecogs.com/png.latex?3%5E2%20%5CRightarrow%202%5E2%20&plus;%202*2%20&plus;%201%20%3D%209). This is easy.

The interesting bit is the "forward" delta which is our arithmetic series of odd numbers as seen above: 
![equation](http://latex.codecogs.com/png.latex?%28N%5E2%29%20-%20%28N-1%29%5E2%20%3D%202N&plus;1)

But if we are going backwards, our "backward" delta for (N-1) will be:
![equation](http://latex.codecogs.com/png.latex?2%28N-1%29&plus;1%20%5Crightarrow%202N%20-2%20&plus;%201%20%5Crightarrow%202N-1)
which means we can just store 2N when computing Square(N), and add +1 for the forward delta or decrease with -1 for the backward delta as needed.

To be clearer: If N=3, and you want to go "forward" (N+1), you use:
- ![equation](http://latex.codecogs.com/png.latex?Square%283%29%20&plus;%20%7BForwardDelta%7D%283%29%20%5CRightarrow%209%20&plus;%207%20%5CRightarrow%2016%20%5Cequiv%20Square%284%29)

And if N=3, and you want to go "backward" (N-1), you use:
- ![equation](http://latex.codecogs.com/png.latex?Square%283%29%20-%20%7BBackwardDelta%7D%283%29%20%5CRightarrow%209%20-%205%20%5CRightarrow%204%20%5Cequiv%20Square%282%29)

So the arithmetic "forward" progression is then:
|             |||||||||||
| ----------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|          N: |   1|  2|  3| 4 | 5 |  6 |  7 |  8 |  9 | 10 |
|     Square: |   1| 4| 9| 16| 25| 36| 49| 64| 81| 100 |
|Progression [Square(N) - Square(N-1)]: |   1| 3| 5| 7| 9| 11| 13| 15| 17| 19 |

Therefore, for a given number N, the backward progression is 2N-1, or in other words, 2*(N-1) + 1.
(i.e. 1 + 2+2+...+2 n-1 times).

So we see that for each number N, its power of 2 will be the power of two of the previous number, plus a constant (2N-1).

And the square of each number is always the progression, plus the previous number squared, recursively as follows:
- ![equation](http://latex.codecogs.com/png.latex?Progression%28N%29%20%5Crightarrow%20Progression%28N-1%29%20&plus;%202%20%3D%20%28N*2-1%29)
- ![equation](http://latex.codecogs.com/png.latex?Square%28N%29%20%3D%20Progression%28N%29%20&plus;%20Square%28N-1%29%2C%20%5Cforall%20N)

#### NOTE: As we will be using recursion and we want to avoid multiplications, we will assume N>=0.

| N   |              Prog |   Square | Result| Comments |
| :---: | -----------------: | :--------: | :-----: | :-------- |
|.     |                   |          |       |          |
|.     |                   |          |       |          |
|-2    |             -5|  (-5 + 9) | {  4}|              |
|-1    |            -3|  (-3 + 4) | {  1}|              |
| 0    |            -1|  (-1 + 1) | {  0}|              |
| 1    |             1|  ( 1 + 0) | {  1}|              |
| 2    |             3|  ( 3 + 1) | {  4}  | 3 is previous Prog (1) + 2|
| 3    |             5|  ( 5 + 4) | {  9}  | 5 is previous Prog (3) + 2|
| 4    |             7|  ( 7 + 9) | { 16}  | 7 is prev. Prog (5) + 2|
| 5    |              9|  ( 9 + 16) |{ 25} |  and so on... |
| 6    |             11|  (11 + 25)| { 36}|              |
| 7    |             13|  (13 + 36)| { 49}|              |
| 8    |             15|  (15 + 49)| { 64}|              |
| 9    |             17|  (17 + 64)| { 81}|              |
|10    |             19|  (19 + 81)| {100}|              |
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
