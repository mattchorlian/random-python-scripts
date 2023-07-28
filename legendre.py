#!/usr/bin/env python3
"""
Simple python file for printing primes between n^2 and (n+1)^2
"""
import matplotlib.pyplot as plt


__author__ = "Matt Chorlian"
__version__ = "0.1.0"
__license__ = "MIT"

def legendre_intervals():
    found = True
    for i in range(2, 10000):
        if not found:
            print(f"Could not find prime for n = {i}")
            break
        found = False
        for k in range(i**2, (i+1)**2):
            if is_prime(k):
                found = True
                print("*******************************")
                print(f"For n = {i} -> range({i**2}, {(i+1)**2}): ")
                print(f"PRIME: {k}")
                print("")
                break


def count_legendre_primes():
    counts = []
    for i in range(2, 1000):
        count = 0
        for k in range(i**2, (i+1)**2):
            if is_prime(k):
                count += 1
        counts.append(count)

    return counts



def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True    

def main():
    """ Main entry point of the app """
    legendre_intervals()
    interval_counts = count_legendre_primes()
    xdata = list(range(998))
    plt.scatter(xdata, interval_counts, c='r', label='data')
    plt.title("Count of primes in each integer square gap")
    plt.show()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()