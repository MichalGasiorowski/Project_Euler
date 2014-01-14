#Let d(n) be defined as the sum of proper divisors of 
#n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ? b, then a and b are an amicable 
#pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 
#1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

#################
#To get the sum of divisors consider the following: if n = 220 say, then n = 2^2 * 5^1 * 11^1
#and the sum of its divisors is given by
# d(n) = (2^3-1)   (5^2-1)   (11^2-1)
#        ------- * ------- * -------- = 284 ##### 7 * 6 * 12 = 
#           1        4          10
# and this can be generalized once we know the prime factors of the number.
################


import itertools
import math
from operator import mul
from functools import reduce

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
                if numbers[i] == 0: # This is a prime number
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

def factorize(n,sieveTable):
        if n <=1:
            return [1]
        dividers = []
        if sieveTable != None:
                primes = sieveTable
        else:
                primes = generateSieve(max(math.sqrt(n),100))
        factored = n
        i=0
        while (i < len(primes) )& (i < n):
                if factored % primes[i] ==0:
                        factored /= primes[i]
                        dividers.append(primes[i])
                        continue
                i +=1
        if factored != 1:
                dividers.append(int(factored))
        if dividers[-1] != n:
            dividers.append(n)
        return dividers

#primeFactors = factorize(divToKill,initSieve)
##k=2 # po ile w kombinacjach
        #print ('factors:',factors,'currTriangleNum:',currTriangleNum)
        #while k <= len(primeFactors):
            #combs = list(itertools.combinations(primeFactors,k))
            #for tup in combs:
            #    #print ('tup:',tup)
            #    factors.add(reduce(mul,tup))
            #k+=1


def getDivisors(n,sieve):
    #Proper divisors < n, with 1
    sieveTable = sieve
    maxSieveSize = math.sqrt(n)
    if sieveTable == None:
        sieveTable = generateSieve(maxSieveSize)
    else:
        if sieve[-1] < maxSieveSize:
            sieveTable = generateSieve(maxSieveSize)
    factorsSet = set([1])
    primeFactors = factorize(n,sieveTable)
    primeFactors.remove(n)
    uniqueFactors = set(primeFactors)
    factorsSet = factorsSet.union(uniqueFactors)
    #print (factorsSet,primeFactors)
    k=2
    while k < len(primeFactors):
            combs = list(itertools.combinations(primeFactors,k))
            #print (combs)
            for tup in combs:
                #print ('tup:',tup, factorsSet)
                factorsSet.add(reduce(mul,tup))
            k+=1
    return list(factorsSet)
            
def getAmiableNumbersToN(n):
    
    maxSieveSize = math.sqrt(n)
    sieve = generateSieve(1.3*maxSieveSize)
    amiableList = []
    amiableSet = set([])
    num = 1
    cacheOfAmiablesFactorSum = [0] * n
    while num < n:
        divs = getDivisors(num,sieve)
        cacheOfAmiablesFactorSum[num] = sum(divs)
        num +=1
    i=1
    print("divs", divs)
    while i < n:
        if i in amiableSet:
            i+=1
            continue
        amToCheck = cacheOfAmiablesFactorSum[i]
        if amToCheck > n:
            i+=1
            continue
        if (cacheOfAmiablesFactorSum[amToCheck] == i) & (i !=amToCheck) :
            amiableSet.add(i)
            amiableSet.add(amToCheck)
            amiableList.append((i,amToCheck))
        i+=1
    return amiableList,amiableSet, sum(amiableSet)

def main():
    print(getAmiableNumbersToN(10000))
if __name__== "__main__":
    main()


