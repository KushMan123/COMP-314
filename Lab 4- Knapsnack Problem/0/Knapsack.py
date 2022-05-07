def K_BruteForce(n,m,p,w):
    #n=no of objects, m=capacity, p=profit and w=weight
    possible_combinations=pow(2,n)
    max_profit=0
    max_weight=0
    for i in range(0, possible_combinations):
        binary=bin(i)[2:]
        profit=0
        weight=0
        while len(binary)!=n:
            binary="0"+binary
        for j in range(0, len(binary)):
            profit=profit+int(binary[j])*p[j]
            weight=weight+int(binary[j])*w[j]
        if weight>max_weight and weight<=m and profit>=max_profit:
            max_profit=profit
            max_weight=weight
            combination=binary
    return (max_profit, max_weight, combination)

def DynamicPrograming(n,m,p,w):
    value=[]
    for i in range(0,n):
        value.append((w[i],p[i]))
    value=sorted(value, key=lambda a:a[0])
    sorted_p=[]
    sorted_w=[]
    for i in range(0,len(value)):
        sorted_p.append(value[i][1])
        sorted_w.append(value[i][0])
    return KnapSnack(n,m,sorted_p,sorted_w)

def KnapSnack(n,m,p,w):
    K=[[0 for i in range(m+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                K[i][j]=0
            elif w[i-1]<=j:
                K[i][j] =max(p[i-1]+K[i-1][j-w[i-1]],K[i-1][j])
            else:
                K[i][j]=K[i-1][j]
    profit=K[n][m]
    while(n !=0):
        if K[n][m] != K[n-1][m]:
            print("Package with weight", w[n-1], "and profit", p[n-1]) 
            m=m-w[n-1]
        n=n-1
    return profit

if __name__=="__main__":
    w_2=[12,2,1,1,4]
    p_2=[4,2,1,2,4]
    m_2=15
    n_2=len(w_2)
    print("-------------------Dynamic-----------------------")
    print(DynamicPrograming(n_2,m_2,p_2,w_2))
    print("-------------------Brute Force-------------------")
    print(K_BruteForce(n_2,m_2,p_2,w_2))