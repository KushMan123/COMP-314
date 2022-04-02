from binary_search import binary_search
import random
import matplotlib.pyplot as plt
import time

def WorstCaseBinarySearch():
    array_size=[]
    time_taken=[]
    print("Worst Case")
    for size in range(0,110000,10000):
        values=sorted(random.sample(range(0,size),size))
        if not values:
            array_size.append(size)
            time_taken.append(0)
        else:
            target=values[-1]
            t1=time.perf_counter()
            binary_search(0, len(values)-1,values,target)
            t2=time.perf_counter()            
            array_size.append(size)
            time_taken.append((t2-t1))
    return [array_size,time_taken]

def BestCaseBinarySearch():
    array_size=[]
    time_taken=[]
    print("Best Case")
    for size in range(0,110000,10000):
        values=sorted(random.sample(range(0,size),size))
        if not values:
            array_size.append(size)
            time_taken.append(0)
        else:
            target=values[size//2-1]
            t1=time.perf_counter()
            binary_search(0, len(values)-1,values,target)
            t2=time.perf_counter()
            array_size.append(size)
            time_taken.append((t2-t1))
    return [array_size,time_taken]


if __name__=="__main__":
    worstCase=WorstCaseBinarySearch();
    bestCase=BestCaseBinarySearch();
    worstCase,=plt.plot(worstCase[0],worstCase[1],'r')
    bestCase,=plt.plot(bestCase[0],bestCase[1],'b')
    plt.xlabel("Input Size")
    plt.ylabel("Time Taken")
    plt.legend([worstCase,bestCase],["Worst Case", "Best Case"])
    plt.show()