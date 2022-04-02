from binary_search import binary_search
import time
import random

def binary_search_time():
    values=sorted(random.sample(range(0,100000),10000))
    for i in range(0,10):
        t1=time.time()
        target=random.choice(values)
        index=binary_search(0, len(values),values,target)
        print("Index of", target,"=",index )
        print("Time taken:", (time.time()-t1)*1000, "ms")

if __name__=="__main__":
    binary_search_time()