import sys

primes = [2]


#  Function loops through already known prime and upto to root of the number
def is_prime(num: int) -> bool:
    for prime in primes:
        if prime > num ** (1 / 2):
            return True
        if num % prime == 0:
            return False
    return True


if __name__ == "__main__":
    number = 50000
    if len(sys.argv) == 2:
        number = int(sys.argv[1])
    for num in range(3, number, 2):
        if is_prime(num):
            primes.append(num)

    print(len(primes))
