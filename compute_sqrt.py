#!/usr/bin/env python3.8
import sys
import math

def approximation_error(N, X):
    """Returns the absolute, relative, and percent error of an approximation X to N"""
    absolute_error = abs(N - X)
    relative_error = abs(1 - (X / N))
    percent_error = abs((N-X)/N)*100
    return (absolute_error, relative_error, percent_error)

def sqrt(N, X=None, iterations=0):
    """
    Newton's method:
    X = some random number between [0, N]
    while abs(N - (X**2)) > ERROR:
        X = X - ((X**2 - N) / (2 * X))
    """
    if N < 0:
        result = sqrt(-N, X, iterations)
        return (complex(result[0], 1), result[1], result[2], result[3], result[4])
    if N == 0: return (0, iterations, 0, 0, 0)
    if N == 1: return (1, iterations, 0, 0, 0)
    if not X: X = N/2 # seeding our first X ... it can be any number [0,N]
    while abs(N - X**2) > sqrt.error:
        X = X - ((X**2 - N) / (2 * X))
        iterations += 1
    absolute_error, relative_error, percent_error = approximation_error(math.sqrt(N), X)
    return (X, iterations, absolute_error, relative_error, percent_error)
sqrt.error = 0.000000000001

def recursive_sqrt(N, X=None, iterations=0):
    """
    Newton's method:
    X = some random number between [0, N]
    while abs(N - (X**2)) > ERROR:
        X = X - ((X**2 - N) / (2 * X))
    """
    if N < 0:
        result = recursive_sqrt(-N, X, iterations)
        return (complex(result[0], 1), result[1], result[2], result[3], result[4])
    if N == 0: return (0, iterations, 0, 0, 0)
    if N == 1: return (1, iterations, 0, 0, 0)
    if not X: X = N/2 # seeding our first X ... it can be any number [0,N]
    X_square = X ** 2
    #print('{:20.012f} {:^12d} {:>20.012f}'.format(X, N, abs(N - X_square)))
    newX = X - ((X_square - N) / (2*X)) 
    newX_square = newX ** 2
    if abs(N - newX_square) <= sqrt.error:
        return (newX, iterations)
    return recursive_sqrt(N, newX, iterations+1, 0, 0, 0)
recursive_sqrt.error = 0.000000000001

def sqrt_binary_search(N, low=0, high=None, iterations=0):
    """
    Binary search method:
        low = 0
        high = N
        mid = 0
        until N - (low + mid)^2 <= ERROR:
            mid = (high - low) / 2
            x0 = (low + mid) ^ 2
            if x0 > N:
                low = low
                high = high - mid
            else:
                low = low + mid
                high = high
        return low + mid
    """
    if N < 0:
        result = sqrt_binary_search(-N, low, high, iterations)
        return (complex(result[0], 1), result[1], result[2], result[3], result[4])
    if N == 0: return (0, iterations, 0, 0, 0)
    if N == 1: return (1, iterations, 0, 0, 0)
    high = N if not high else high
    mid = 0
    while abs(N - (low + mid)**2) > sqrt_binary_search.error:
        mid = (high - low) / 2
        newX_square = (low + mid) ** 2
        #print('{:20.012f} {:^12d} {:>20.012f} {:>20.012f} {:>20.012f}'.format(mid, N, abs(N - newX_square), low, high))
        if newX_square > N:
            high = high - mid
        else:
            low = low + mid
        iterations += 1
    absolute_error, relative_error, percent_error = approximation_error(math.sqrt(N), low+mid)
    return (low + mid, iterations, absolute_error, relative_error, percent_error)
sqrt_binary_search.error = 0.000000000001

def recursive_sqrt_binary_search(N, low=0, high=None, iterations=0):
    if N < 0:
        result = recursive_sqrt_binary_search(-N, low, high, iterations)
        return (complex(result[0], 1), result[1], result[2], result[3], result[4])
    if N == 0: return (0, iterations, 0, 0, 0)
    if N == 1: return (1, iterations, 0, 0, 0)
    high = N if not high else high
    mid = (high - low) / 2
    newX_square = (low + mid) ** 2
    #print('{:20.012f} {:^12d} {:>20.012f} {:>20.012f} {:>20.012f}'.format(mid, N, abs(N - newX_square), low, high))
    if abs(N - newX_square) <= recursive_sqrt_binary_search.error:
        return (low + mid, iterations)
    if newX_square > N:
        return recursive_sqrt_binary_search(N, low, high - mid, iterations+1)
    return recursive_sqrt_binary_search(N, low + mid, high, iterations+1)
recursive_sqrt_binary_search.error = 0.000000000001

if __name__ == '__main__':
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
        result, iterations, absolute_error, relative_error, percent_error = sqrt(N)
        print(f'newton: sqrt({N}) = {result:<20.12f} : {iterations} iterations.')
        result, iterations, absolute_error, relative_error, percent_error = sqrt_binary_search(N)
        print(f'binary: sqrt({N}) = {result:<20.12f} : {iterations} iterations.')
        sys.exit(0)

    for N in range(0, 1000+1):
        result, iterations, absolute_error, relative_error, percent_error = sqrt(N)
        result2, iterations2, absolute_error, relative_error, percent_error = sqrt_binary_search(N)
        winner = 'newton' if iterations < iterations2 else 'binary'
        error = 0.00000000001
        matches = " " if abs(result - result2) <= error else "X"
        #print(abs(result-result2), error, abs(result-result2) <= error)
        print(f'{matches} sqrt({N:>04d}) = newton:{result:>20.12f}    -    binary:{result2:>20.12f} .... {iterations:>4d} vs {iterations2:>4d} iterations   Best: [{winner}]')

