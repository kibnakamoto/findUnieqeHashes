from hashlib import sha256
from time import time

# how to generate data from 0 to 2^256? until hash equals zero
# this is to find all possible combinations which is impossible
global unique_hash
global hash_size_limit
start_time = time()

# TODO: start from zero in beggining, then start from last largest i value

## approximate amount of combinations to go through
# raise Exception(int(2**256-146030454))
## approximate amount of days left if iteration continues for 30 minutes
# raise Exception(int(2**256/146030454))
## approximate amout of days left if iteration continued 24 hours a day
# raise Exception(int(2**256/(50000000*6*24)))

def find_unique_hash():
    timer = time()
    limit = 64; # smallest limit until now
    smallest_hash = 2**256
    for i in range(182980442,2**256):
        gen_hash = sha256(str(i).encode()).hexdigest()
        
        if int(gen_hash,16) <= 2**200:
            unique_hash = int(gen_hash,16)
            hash_size_limit = 2**200
            end_time = time()
            print("hash: ", unique_hash)
            print("i: ", i)
            print("time: ", end_time-start_time)
        elif int(gen_hash,16) <= 2**150:
            unique_hash = int(gen_hash,16)
            hash_size_limit = 2**150
            end_time = time()
            print("hash: ", unique_hash)
            print("i: ", i)
            print("time: ", end_time-start_time)
        elif int(gen_hash,16) <= 2**100:
            unique_hash = int(gen_hash,16)
            hash_size_limit = 2**100
            end_time = time()
            print("hash: ", unique_hash)
            print("i: ", i)
            print("time: ", end_time-start_time)
        elif int(gen_hash,16) <= 2**50:
            unique_hash = int(gen_hash,16)
            hash_size_limit = 2**100
            end_time = time()
            print("hash: ", unique_hash)
            print("i: ", i)
            print("time: ", end_time-start_time)
        elif int(gen_hash,16) == 0:
            unique_hash = int(gen_hash,16)
            hash_size_limit = 0
            end_time = time()
            print("hash: ", unique_hash)
            print("i: ", i)
            print("time: ", end_time-start_time)
            break
        else:
            if timer+1 <= time(): # if one second passed, print time
                print("tm: ", time()-start_time, end="\t")
                print("curr i: ", i)
                timer = time()

        if int(gen_hash,16) <= smallest_hash:
            print("ch: ", gen_hash, "\t\t\tlen: ", len(hex(int(gen_hash,16))[2:]))
            print("i: ", i)
            smallest_hash = int(gen_hash,16)
            smallest_hash_i = i;
            limit = len(hex(int(gen_hash,16))[2:])
        
        # print smallest values right before termination
        if time()-start_time == 599:
            print("l: ", limit)
            print("sh: ", smallest_hash);
            print("sh i: ", smallest_hash_i);

find_unique_hash()
print("loop ended, i = 2**256") # impossible

# around 50 million combinations tried per 10 minutes

########## TESTS ##########
"""
day 1:
 1. killed at tm = 599.153, i = 48,124,918
 2. killed at tm = 599.294, i = 97,881,618
 3. killed at tm = 599.389, i = 146,030,454
day 2:
 1. killed at tm = 599.438, i = 182,980,442
 2. 
 3. 
"""
