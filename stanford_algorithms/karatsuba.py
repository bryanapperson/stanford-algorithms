#!/usr/bin/env python
"""Multiply numbers using Karatsuba multiplication"""
from __future__ import division
from math import log10
import sys


def karatsuba(num1, num2):
    """Recursive Karatsuba implementation.
    
    Created for the Coursera Stanford Algorithms specialization.
    Based on:
    https://en.wikipedia.org/wiki/Karatsuba_algorithm#Pseudocode
    
    :param num1: A positive integer
    :type num1: int
    :param num2: A positive integer
    :type num2: int
    """
    if (num1 < 10) or (num2 < 10):
        return num1 * num2
    else:
        # Calculate the size of numbers
        m = max(int(log10(num1)) + 1, int(log10(num2)) + 1)
        m2 = m // 2
        high1 = num1 // 10**m2
        high2 = num2 // 10**m2
        low1 = num1 % 10**m2
        low2 = num2 % 10**m2
        z0 = karatsuba(low1, low2)
        z1 = karatsuba((low1 + high1), (low2 + high2))
        z2 = karatsuba(high1, high2)
        return (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0


if __name__ == '__main__':
    try:
        print(karatsuba(sys.argv[1], sys.argv[2]))
    except KeyError:
        print('This script requires two nmumbers to multiply as arguments.')
        sys.exit(1)

