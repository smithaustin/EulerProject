from euler.primes import get_ascending_primes

def sum_primes(max):
    """Sums all primes under a given value (exlcusive)"""
    return sum(get_ascending_primes(max))

if __name__ == "__main__":
    print(sum_primes(2000000))

    