def Merge_Sort(values,p,r):
    if p<r:
        q=(p+r)//2
        Merge_Sort(values,p,q)
        Merge_Sort(values,q+1,r)
        Merge(values,p,q,r)
        return values

def Merge(values,p,q,r):
    n1=q-p+1
    n2=r-q
    L,R=list(),list()
    for i in range(0,n1):
        L.append(values[p+i])
    for j in range(0,n2):
        R.append(values[q+j+1])
    i,j=0,0
    for k in range(p,r):
        if L[i]<=R[j]:
            values[k]=L[i]
            i+=1
            if i==n1:
                while j<n2:
                    values[k+1]=R[j]
                    j+=1
                    k+=1
                break
        else:
            values[k]=R[j]
            j+=1
            if j==n2:
                while i<n1:
                    values[k+1]=L[i]
                    i+=1
                    k+=1
                break
    return values