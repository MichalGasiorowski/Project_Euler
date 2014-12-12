#2520 is the smallest number that can be divided by each 
#of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#NWW
# 1* 2* 3* 4 *5 *6 *7 *8* 9 *10

# 1 * 2 * 3 * (2 * 2) * 5 * (2 * 3) * 7 * (2*2*2) * (3* 3) * (2*5)

def div(a,b):
    d = int(a/b)
    return d,d*b

def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b,a - b*int(a/b))

def lcm(a,b):
    return int((a*b)/gcd(a,b))

def findMinMult(n):
    ret = 1
    i=1
    while i <=n:
        ret = lcm(ret,i)
        i+=1
    return ret




