import math


def generate_primes(max_num):
    if max_num is None:
        raise TypeError('max_num cannot be None')
    array = [True] * max_num
    array[0] = False
    array[1] = False
    prime = 2
    while prime <= math.sqrt(max_num):
        _cross_off(array, prime)
        prime = _next_prime(array, prime)
    return array


def _cross_off(array, prime):
    for index in range(prime * prime, len(array), prime):
        # Start with prime*prime because if we have a k*prime
        # where k < prime, this value would have already been
        # previously crossed off
        array[index] = False


def _next_prime(array, prime):
    next = prime + 1
    while next < len(array) and not array[next]:
        next += 1
    return next