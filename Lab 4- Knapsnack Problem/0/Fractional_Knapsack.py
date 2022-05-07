def F_BruteForce(n,m,p,w):
    #n=no of objects, m=capacity, p=profit and w=weight
    possible_combinations=pow(2,n)
    max_profit=0
    max_weight=0
    max_fractional_profit=0
    for i in range(0, possible_combinations):
        binary=bin(i)[2:]
        profit=0
        weight=0
        while len(binary)!=n:
            binary="0"+binary
        for j in range(0, len(binary)):
            profit=profit+int(binary[j])*p[j]
            weight=weight+int(binary[j])*w[j]
        if weight<=m and profit>=max_profit:
            max_profit=profit
            max_weight=weight
            combination=binary
    remaining_weight=m-max_weight
    if remaining_weight!=0:
        fractional_profit=0
        for k in range(0, len(combination)):
            if combination[k]=="0":
                fractional_profit=(p[k]/w[k])*remaining_weight
                if fractional_profit>=max_fractional_profit:
                    max_fractional_profit=fractional_profit
    max_profit=max_profit+max_fractional_profit
    max_weight=max_weight+remaining_weight
    return (max_profit,max_weight,combination)


def GreedyAlgorithm(n,m, p,w):
    #n=no of objects, m=capacity, p=profit and w=weight
    cost=[]
    for i in range(0,n):
        cost.append((p[i]/w[i],i))
    cost.sort(reverse=True)
    remaining_weight=m
    i=0
    profit=0
    while remaining_weight > 0 and i<n:
        index=cost[i][1]
        if w[index]<=remaining_weight:
            profit=profit + p[index]
            remaining_weight=remaining_weight-w[index]
            i=i+1
        else:
            profit=profit+cost[i][0]*remaining_weight
            remaining_weight=0
        print("Object Index: ",index, 
        "Profit:",p[index], 
        "Weight: ", w[index],
        "Total Profit: ", profit, 
        "Remaining Weight:", remaining_weight)
    return profit
    

if __name__=="__main__":
    w_1=[3,4,6,5]
    p_1=[2,3,1,4]
    m_1=8
    n_1=len(w_1)
    print("-----------------------BruteForce----------------------")
    print(F_BruteForce(n_1,m_1,p_1,w_1))
    print("--------------------Greedy-----------------------------")
    print(GreedyAlgorithm(n_1,m_1,p_1,w_1))
    