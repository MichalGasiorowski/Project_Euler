#The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def moduloPow(x,y,mod):
    #x^y modulo mod
    ret = 1
    i=0
    while i < y:
        ret = (ret *x) %mod
        i+=1
    return ret

def sumOfPowsWithMod(n,mod):
    i=1
    ret = 0
    while i <= n:
        ret = (ret + moduloPow(i,i,mod) ) % mod
        i+=1
    return ret
