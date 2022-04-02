def linear_search(values,target):
    for i in range (0,len(values)):
        if values[i]==target:
            return i

    return -1

