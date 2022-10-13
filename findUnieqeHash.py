from hashlib import sha256
import secrets
#from numba import jit, njit, cuda 
from timeit import default_timer as timer
import multiprocessing
import os


## approximate amount of combinations to go through
# raise Exception(int(2**256-146030454))
## approximate amount of days left if iteration continues for 30 minutes
# raise Exception(int(2**256/146030454))
## approximate amout of days left if iteration continued 24 hours a day
# raise Exception(int(2**256/(50000000*6*24)))

count = multiprocessing.Queue()
limit = 0x10000000000000000000000000000000000000000000000000000000000000000
smallest_hashes = multiprocessing.Queue()
for i in range(18):
    smallest_hashes.put(limit)
time = int(input("input how long the calculation should last: "))

def find_unique_hash(smallest_hash, count_, time):
    start = timer()
    loop_end_limit = 0x10000000000000000000000000000000000000000000000000000000000000000
    limit = 64; # smallest limit until now
    printed_unique_value = False
    randbelow = 0x10000000000000000000000000000000000000000000000000000000000000000
    smallest_hash_i = 0x10000000000000000000000000000000000000000000000000000000000000000
    
    for i in range(loop_end_limit):
        nonce = secrets.randbelow(randbelow)
        gen_hash = sha256(hex(nonce)[2:].encode('utf-8')).hexdigest()
        #if start+119.5 <= timer(): 
        #    # if 75 seconds passed, print time and current i
        #    print(f"tm: {timer()-start_time}\tcurr i: {i}")
        #    start = timer()
        hash_ = int(gen_hash, 16)
        if hash_ < smallest_hash_i:
        #    limit = len(hex(int(gen_hash,16))[2:])
        #    print(f"ch: {gen_hash}\t\t\tlen: {limit}")
        #    print(f"i: {i}")
        #    smallest_hash = int(gen_hash,16)
            smallest_hash_i = hash_
        if timer() >= start+time:
            print(f"hash generated count: {i}")
            count_.put(i)
            smallest_hash.put(smallest_hash_i)
            break

t1 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t2 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t3 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t4 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t5 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t6 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t7 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t8 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t9 = multiprocessing.Process(target=find_unique_hash,args=[smallest_hashes, count, time])
t10 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 
t11 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 
t12 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 
t13 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 
t14 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 
t15 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 
t16 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 
t17 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 
t18 = multiprocessing.Process(target=find_unique_hash, args=[smallest_hashes, count, time]) 

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()
t16.join()
t17.join()
t18.join()

conv = []
while not smallest_hashes.empty():
    conv.append(smallest_hashes.get())

sm_hash = min(conv)
all_count = 0

while not  count.empty():
    all_count += count.get()

print(f"total hashes generated: {all_count}")
print(f"smallest hash generated: 0x{hex(sm_hash)[2:].zfill(64)}")
print(f"hashrate: {all_count//time}")


# around 50 million combinations tried per 10 minutes on online interpreter without GPU

########## TESTS ON SINGLE-THREAD ONLINE INTERPRETER ##########
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
