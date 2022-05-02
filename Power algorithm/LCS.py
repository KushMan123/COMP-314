def Memoization(A,B):
    m=len(A)+1
    n=len(B)+1
    X=[[-1]*n for i in range(0,m)]
    return LCS(A,B,0,0,X)

def LCS(A,B,m,n,X):
    if m<len(A) and n<len(B):
        char1=A[m]
        char2=B[n]
    if m==len(A) or n==len(B):
        X[m][n]=0
        return X[m][n]
    if X[m][n] != -1:
        return X[m][n]
    if A[m]==B[n]:
        X[m][n]=1+LCS(A,B,m+1,n+1,X)
        return X[m][n]
    else:
        X[m][n]=max(LCS(A,B,m+1,n,X),LCS(A,B,m,n+1,X))
        return X[m][n]

if __name__=="__main__":
    A="PRESIDENT"
    B="PROVIDENCE"
    print(Memoization(A,B))