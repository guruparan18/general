primes = [2]


def is_prime(num: int) -> bool:
    for prime in primes:
        if prime > num ** (1 / 2):
            return True
        if num % prime == 0:
            return False
    return True


if __name__ == "__main__":
    for num in range(3, 50000, 2):
        if is_prime(num):
            primes.append(num)

    print(len(primes))
