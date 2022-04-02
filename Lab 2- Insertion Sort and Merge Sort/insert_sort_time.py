import random
import matplotlib.pyplot as plt
import time
from insertion_sort import Insertion_Sort

def WorstCaseInsertionSort():
    array_size=[]
    time_taken=[]
    print("Worst Case")
    for i in range(0,11000,1000):
        values=sorted(random.sample(range(0,i),i),reverse=True)
        if not values:
            array_size.append(i)
            time_taken.append(0)
        else:
            t1=time.perf_counter()
            Insertion_Sort(values)
            t2=time.perf_counter()
            print("Input Size:",i,"Time Taken:",t2-t1)
            array_size.append(i)
            time_taken.append(t2-t1)
    return [array_size,time_taken]

def BestCaseInsertionSort():
    array_size=[]
    time_taken=[]
    print("Best Case")
    for i in range(0,11000,1000):
        values=sorted(random.sample(range(0,i),i))
        if not values:
            array_size.append(i)
            time_taken.append(0)
        else:
            t1=time.perf_counter()
            Insertion_Sort(values)
            t2=time.perf_counter()
            print("Input Size:",i,"Time Taken:",t2-t1)
            array_size.append(i)
            time_taken.append((t2-t1)*1000)
    return [array_size,time_taken]

if __name__=="__main__":
    worstCase=WorstCaseInsertionSort();
    bestCase=BestCaseInsertionSort();
    worstCase,=plt.plot(worstCase[0],worstCase[1],'r')
    bestCase,=plt.plot(bestCase[0],bestCase[1],'b')
    plt.xlabel("Input Size")
    plt.ylabel("Time Taken")
    plt.legend([worstCase,bestCase],["Worst Case", "Best Case"])
    plt.show()
        