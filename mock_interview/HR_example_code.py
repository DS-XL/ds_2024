# question 1: https://www.hackerrank.com/challenges/flipping-bits

def flippingBits(n):
    # simple string manipulation method
    n_binary = bin(n)
    n_bin_32 = n_binary[2:].zfill(32)
    return int(n_bin_32.replace('0','a').replace('1', '0').replace('a', '1'), base=2)

def flippingBits(n):
    # this number is (2**32)-1
    # unsigned integers given which is 32
    # 2**32 = 4294967296
    # to flip is to just minus 1
    THE_FLIPPING = 4294967295

    # ^ = bitwise XOR
    return n ^ THE_FLIPPING

# question 2: https://www.hackerrank.com/challenges/repeated-string

def repeatedString(s, n):
    s_a = s.count('a')
    s_len = len(s)
    return n // s_len * s_a + s[:n % s_len].count('a')