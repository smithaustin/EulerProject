import math

def get_ascending_primes(max):
    """Returns a list of primes up to the max (exlusive)"""
    isprime = [True for _ in range(max)]
    isprime[0], isprime[1] = False, False
    current_val = 2
    primes = []

    #Apply a Sieve of Eroesthes (I have no idea how to spell this...)
    while current_val < max:
        if isprime[current_val]:
            primes.append(current_val)
            for multiple in range(current_val, max, current_val):
                if multiple == current_val:
                    continue
                isprime[multiple] = False
        current_val += 1
    return primes

def get_divisors(value):
    if value < 1:
        return []
    factors_front = []
    factors_back = []
    for x in range(1,math.floor(math.sqrt(value)+1)):
        if value%x == 0:
            factors_front.append(x)
            factors_back.append(int(value/x))
    factors_back.reverse()
    if factors_front[-1] == factors_back[0]:
        factors_front.pop()
    factors_front.extend(factors_back)
    return factors_front

if __name__ == "__main__":
    for v in range(100):
        print(str(v) + ": " + str(get_divisors(v)))
    
