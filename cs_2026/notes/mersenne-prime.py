"""List Mersenne primes less than 31."""

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def mersenne_primes_below(limit: int):
    result = []
    # exponents p must be prime
    p = 2
    while True:
        m = (1 << p) - 1
        if m >= limit:
            break
        if is_prime(p) and is_prime(m):
            result.append(m)
        p += 1
    return result

if __name__ == '__main__':
    limit = 31
    mp = mersenne_primes_below(limit)
    print(mp)
