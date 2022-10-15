from math import ceil, log

def bigger_pow_2(num: float) -> int:
    if num < 8:
        return 8
    return 2**ceil(log(num))