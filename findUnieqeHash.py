from hashlib import sha256
import secrets
# from numba import jit, njit, cuda 
from timeit import default_timer as timer

# how to generate data from 0 to 2^256? until hash equals zero
# this is to find all possible combinations which is impossible
start_time = timer()

## approximate amount of combinations to go through
# raise Exception(int(2**256-146030454))
## approximate amount of days left if iteration continues for 30 minutes
# raise Exception(int(2**256/146030454))
## approximate amout of days left if iteration continued 24 hours a day
# raise Exception(int(2**256/(50000000*6*24)))

# @jit(target_backend='cuda')
def find_unique_hash():
    start = timer()
    limit = 64; # smallest limit until now
    loop_end_limit = 2**256
    smallest_hash = loop_end_limit
    printed_unique_value = False
    randbelow = 2**1024
    for i in range(loop_end_limit):
        nonce = secrets.randbelow(randbelow)
        gen_hash = sha256(hex(nonce)[2:].encode('utf-8')).hexdigest()
        if start+119.5 <= timer() and timer()-start_time < 600: 
            # if 75 seconds passed, print time and current i
            print(f"tm: {timer()-start_time}\tcurr i: {i}")
            start = timer()
        
        
        if int(gen_hash,16) < smallest_hash:
            limit = len(hex(int(gen_hash,16))[2:])
            print(f"ch: {gen_hash}\t\t\tlen: {limit}")
            print(f"i: {i}")
            smallest_hash = int(gen_hash,16)
            smallest_hash_i = i;
find_unique_hash()
print("loop ended, i = 2**256") # impossible

# around 50 million combinations tried per 10 minutes on online interpreter without GPU
# around 16 million combinations tried per 10 seconds on laptop with GPU

########## TESTS ON ONLINE INTERPRETER ##########
"""
day 1:
 1. killed at tm = 599.153, i = 48,124,918 # smallest hash value = is 57 digits
 2. killed at tm = 599.294, i = 97,881,618 # smallest hash value = is 57 digits
 3. killed at tm = 599.389, i = 146,030,454 # smallest hash value = is 58 digits
day 2:
 1. killed at tm = 599.438, i = 182,980,442 # smallest hash value is 58 digits
 2. killed at tm = 540.051, i = 304,209,975 # smallest hash value is 58 digits
 3. killed at tm = 599.061, i = 426,479,724 # smallest hash value is 56 digits, first value is largest
 4. killed at tm = 597.500, i = 557,589,673 # smallest hash value is 56 digits, same value as previous
 5. killed at tm = 597.551, i = 689,065,462 # smallest hash value is 58 digits
 6. killed at tm = 597.559, i = 824,162,261, smallest hash value is 58 digits
 7. killed at tm = 597.500, i = 960,251,933 # smallest hash value is 57 digits
 8. killed at tm = 597.519, i = 1,097,552,799 # smallest hash value is 58 digits
"""
