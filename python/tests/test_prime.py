from src import primes


def test_prime():
    assert primes.is_prime(3) is True
    assert primes.is_prime(101) is True
    assert primes.is_prime(100) is False

