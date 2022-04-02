from linear_search import linear_search
import random
import matplotlib.pyplot as plt
import time

def WorstCaseLinearSearch():
    array_size=[]
    time_taken=[]
    for size in range(0,110000,10000):
        values=random.sample(range(0,size),size)
        if not values:
            array_size.append(size)
            time_taken.append(0)
        else:
            target=values[-1]
            t1=time.perf_counter()
            linear_search(values,target)
            t2=time.perf_counter()
            print(t1,t2,t2-t1)
            array_size.append(size)
            time_taken.append(t2-t1)
    return [array_size,time_taken]

def BestCaseLinearSearch():
    array_size=[]
    time_taken=[]
    for size in range(0,110000,10000):
        values=random.sample(range(0,size),size)
        if not values:
            array_size.append(size)
            time_taken.append(0)
        else:
            target=values[0]
            t1=time.perf_counter()
            linear_search(values,target)
            t2=time.perf_counter()
            print(t1, t2,t2-t1)
            array_size.append(size)
            time_taken.append(t2-t1)
    return [array_size,time_taken]


if __name__=="__main__":
    worstCase=WorstCaseLinearSearch();
    bestCase=BestCaseLinearSearch();
    worstCase,=plt.plot(worstCase[0],worstCase[1],'r')
    bestCase,=plt.plot(bestCase[0],bestCase[1],'b')
    plt.xlabel("Input Size")
    plt.ylabel("Time Taken")
    plt.legend([worstCase,bestCase],["Worst Case", "Best Case"])
    plt.show()