from linear_search import linear_search
import time
import random

def linear_search_time():
    values=random.sample(range(0,100000),10000)
    for i in range (0, 10):
        t1=time.time()
        target=random.choice(values)
        index=linear_search(values,target)
        print("Index of", target,"=",index )
        print("Time taken:", (time.time()-t1)*1000, "ms")

if __name__=="__main__":
    linear_search_time()