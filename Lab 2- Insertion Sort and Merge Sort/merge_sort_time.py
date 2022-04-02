import random 
import time
import matplotlib.pyplot as plt
from merge_sort import Merge_Sort

def TimeComplexity():
    array_size=[]
    time_taken=[]
    for i in range(0,11000,1000):
        values=random.sample(range(0,i),i)
        if not values:
            array_size.append(i)
            time_taken.append(0)
        else:
            t1=time.perf_counter()
            Merge_Sort(values,0,len(values)-1)
            t2=time.perf_counter()
            print("Input Size:",i,"Time Taken:",t2-t1)
            array_size.append(i)
            time_taken.append(t2-t1)
    return [array_size,time_taken]

if __name__=="__main__":
    comlexity=TimeComplexity()
    plt.plot(comlexity[0],comlexity[1])
    plt.xlabel("Input Size")
    plt.ylabel("Time Taken")
    plt.show()
    
