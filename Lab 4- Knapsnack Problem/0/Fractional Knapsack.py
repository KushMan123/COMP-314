def BruteForce(n,m,p,w):
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
        if weight<m:
            remaining_weight=m-weight
            max_fractional_profit=0
            fractional_profit=0
            for k in range(0, len(binary)):
                if binary[k]=="0":
                    fractional_profit=(p[k]/w[k])*remaining_weight
                    if fractional_profit> max_fractional_profit and profit>fractional_profit:
                        max_fractional_profit=fractional_profit
                        index=k
                    else:
                        index="null"
        total_profit=profit+max_fractional_profit
        # print("Combination",binary, "Profit",profit,"Weight",weight,"Fractional Profit",max_fractional_profit,"Index",index, "Remaining_Weight", remaining_weight, "Totoal profit",total_profit)
        
        if  total_profit>=max_profit and weight<=m and index != "null":
            max_profit=total_profit
            max_weight=weight+remaining_weight
            combination=binary
    return max_profit,max_weight,combination


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
        print("Object Index: ",index, "Profit:",p[index], "Weight: ", w[index],"Total Profit: ", profit, "Remaining Weight:", remaining_weight)
    

if __name__=="__main__":
    p=[12,14,56,8]
    w=[2,7,10,5]
    m=20
    n=len(p)
    profit, weight, combination= BruteForce(n,m,p,w)
    print("-----------------------BruteForce----------------------")
    print(profit, weight, combination)
    print("--------------------Greedy-----------------------------")
    GreedyAlgorithm(n,m,p,w)
    