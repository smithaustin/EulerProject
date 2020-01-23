from math import floor

def power_digit_sum(base, exponent):
    val = base**exponent
    cur_sum = 0
    val_copy = val
    while val_copy:
        cur_sum += val_copy % 10
        val_copy //= 10
    return cur_sum



if __name__ == "__main__":
    print(power_digit_sum(2,2))
    print(power_digit_sum(2,15))
    print(power_digit_sum(2,100))
    print(power_digit_sum(2,1000))