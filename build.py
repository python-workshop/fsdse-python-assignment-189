#Generate a list of primes
def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
x = list(filter(is_prime, range(1, 30)))
print(x)