#!/usr/bin/python3
"""module for functions"""


def isPrime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def countPrime(nums):
    """Count the number of prime numbers in a list."""
    count = 0
    for num in nums:
        if isPrime(num):
            count += 1
    return count


def isWinner(x, nums):
    """Determine the winner based on prime number count."""
    ben = 0
    maria = 0
    if x <= 0 or not nums:
        return None
    for num in range(x):
        num_arr = [n for n in range(1, nums[num] + 1)]
        if countPrime(num_arr) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if ben == maria:
        return None
    return "Maria"
