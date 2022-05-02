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
        if weight>max_weight and weight<=m:
            max_profit=profit
            max_weight=weight
            combination=binary
    return max_profit, max_weight, combination

if __name__=="__main__":
    p=[12,14,56,8]
    w=[2,7,10,5]
    m=20
    n=len(p)
    profit, weight, combination= BruteForce(n,m,p,w)
    print(profit, weight, combination)