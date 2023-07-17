#!/usr/bin/env python3

import numpy as np

# def munge(val):
#     x = val.copy()
#     x *= 32
#     x += 0x7fffffff
#     return x

# def to_int32(val):
#     return np.array((val,), dtype=np.int32)

# print(munge(to_int32(3)))

a = 10;
b = 20;

def bit_MUL(a,b):
	a_bin = 


def bitwise_multiply(a, b):
    result = 0
    for i in range(32):
        if (b & 1) == 1:
            result += a
        a <<= 1
        b >>= 1
    return result

# Example usage
num1 = 10  # Binary: 00000000000000000000000000001010
num2 = 5   # Binary: 00000000000000000000000000000101

result = bitwise_multiply(num1, num2)
print(f"The result of {num1} * {num2} is: {result}")
