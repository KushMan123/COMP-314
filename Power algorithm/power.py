import math

def power(a,n):
    if n == 0:
        return 1
    if n>0:
        base=a
    if n<0:
        base=1/a
    x=power(base,math.floor(abs(n)/2))
    if n%2==0:
        return x*x
    else:
        return x*x*base    


if __name__=="__main__":
    print(power(2,8))