from math import sqrt
from euler.primes import get_divisors

def triangle_number_by_num_factors(min_factors):
    triangle_number = 0
    next_value = 1
    factors_len = 0
    while not factors_len > min_factors:
        triangle_number += next_value
        next_value += 1
        if sqrt(triangle_number) < min_factors:
            continue
        factors = get_divisors(triangle_number)
        factors_len = len(factors)

    return (triangle_number, factors)
        
if __name__ == "__main__":
    print(triangle_number_by_num_factors(5))
    print(triangle_number_by_num_factors(6))
    print(triangle_number_by_num_factors(10))
    print(triangle_number_by_num_factors(500))