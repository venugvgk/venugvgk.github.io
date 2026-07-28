"""Find Mersenne primes below 100."""


def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2

    return True


def is_mersenne_prime(p):
    """Return True if 2^p - 1 is a prime number."""
    mersenne_number = (2 ** p) - 1
    return is_prime(p) and is_prime(mersenne_number)


def find_mersenne_primes_below(limit):
    """Return a list of Mersenne primes where 2^p - 1 < limit."""
    results = []
    p = 2

    while True:
        mersenne_number = (2 ** p) - 1
        if mersenne_number >= limit:
            break
        if is_mersenne_prime(p):
            results.append(mersenne_number)
        p += 1

    return results


if __name__ == "__main__":
    limit = 100
    primes = find_mersenne_primes_below(limit)
    print("Mersenne primes below 100:")
    for prime in primes:
        print(prime)
