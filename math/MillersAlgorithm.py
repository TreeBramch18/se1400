import random

def is_probable_prime(n, k=10):
    """
    Miller–Rabin probabilistic primality test.
    n: number to test
    k: number of rounds (default: 10)
    Returns: True if probably prime, False if composite.
    """

    # Handle small or simple cases first
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^s * d with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Perform k rounds of testing
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        # Square x repeatedly
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # If we did not break, it's composite
            return False

    # Probably prime
    return True
