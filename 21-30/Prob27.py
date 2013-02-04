##Euler published the remarkable quadratic formula:
##
##n² + n + 41
##
##It turns out that the formula will produce 40 primes for the consecutive
##values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
##is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is
##clearly divisible by 41.
##
##Using computers, the incredible formula  n² − 79n + 1601 was
##discovered, which produces 80 primes for the consecutive values
##n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
##
##Considering quadratics of the form:
##
##    n² + an + b, where |a| < 1000 and |b| < 1000
##
##    where |n| is the modulus/absolute value of n
##    e.g. |11| = 11 and |−4| = 4
##
##Find the product of the coefficients, a and b, for the quadratic
##expression that produces the maximum number of primes for consecutive
##values of n, starting with n = 0.

import math
from time import clock
def generateSieve(num):
        n = int(num)
        sieve = []
        numbers = [0] *n
        i=2
        while i < n :
                #print i, sieve
                if numbers[i] == 1:
                        i += 1
                        continue
                if numbers[i] ==0: # This is a prime number
                        sieve.append(i)
                if 2*i >= n:
                        i +=1
                        continue
                j=i
                while True:
                        j += i
                        if j >= n:
                                break
                        numbers[j] = 1
                i += 1
        return sieve
def getValue(a1,a2,a3,n):
    return a1 * n**2 + a2*n + a3

def findMaxPoly(numIn):
    if numIn % 2 == 0:
        num = numIn -1
    else:
        num = numIn 
    maxPrimeNum = 0
    bestCoeffs = (0,0)
    sieve = generateSieve(num * 300)
    sieveSet = set(sieve)
    clockSieveSum=0
    clockInnerSum =0

    indH = numIn
    indL =0
    indF = 0
    indOld = 0
    while True:
        indF = int((indL + indH)/2)
        #print (indL, indF,indH, sieve[indF] )
        if sieve[int((indL + indH)/2)] < num:
            indL = indF
        else:
            indH = indF
        if indF == indOld:
            break
        indOld = indF
    #print(indF)
    maxSieveIndForb = indF
    #print (sieve[500])
    for a in range(-num,num,2):
        for b in sieve[:maxSieveIndForb+1]:
##            clockInner = clockSieve = clock()
            if b not in sieveSet:
##                minus = clock() - clockSieve
##                clockSieveSum += minus
##                clockInnerSum += minus
                continue
##            clockSieveSum += (clock() - clockSieve)
            n = 0
            while True:
                if int(getValue(1,a,b,n)) in sieveSet:
                    n+=1
                else:
                    break
            if n > maxPrimeNum :
                maxPrimeNum = n
                bestCoeffs = (a,b)
##            minus = clock() - clockInner
##            clockInnerSum += minus
            b+=1
        a+=1
    return maxPrimeNum,bestCoeffs#,clockSieveSum,clockInnerSum


start = clock()
solved = findMaxPoly(40000)
print ('Best combo:',solved[0],'Best coefs',solved[1], 'Mult:', solved[1][0]*solved[1][1],'Time:', str(clock() - start)+'s')
##print ('ClockSieveSum:',solved[2], 'ClockInner:',solved[3])
