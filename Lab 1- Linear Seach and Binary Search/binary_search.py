def binary_search(low,high,value,target):
    i=0
    while low <= high:
        mid = (low+high)//2
        print("mid=", mid)
        print("high=", high)
        print("low=",low)
        if value[mid] == target:
            print(i)
            return mid

        elif value[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
        i=i+1
    return -1